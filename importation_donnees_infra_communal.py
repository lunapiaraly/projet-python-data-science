# --- importation des modules ---
import requests
from zipfile import ZipFile
import os
import py7zr
import pandas as pd
import geopandas as gpd


# --- importation ddu dataset sur le niveau de vie et le niveau de pollution par carreaux en
# Ile de France (données Airparif et Insee) ---

def telecharger_donnees():
    print("téléchargement des données (environ 2 minutes)")

    dossier_data = os.path.join(os.path.dirname(__file__), "data_carreaux")
    # --- téléchargement des données carroyées de niveau de vie Insee ---
    URL_INSEE_ZIP = "https://www.insee.fr/fr/statistiques/fichier/7655475/Filosofi2019_carreaux_200m_shp.zip"
    intermediaire_zip = "donnees.zip"
    reponse = requests.get(URL_INSEE_ZIP)
    if reponse.status_code == 200:
        print("téléchargement réussi -> décompression")
        with open(intermediaire_zip, "wb") as f:
            f.write(reponse.content)
        with ZipFile(intermediaire_zip, 'r') as zip_ref:
            zip_ref.extractall(dossier_data)
        chemin_fichier_7z = os.path.join(dossier_data, "Filosofi2019_carreaux_200m_shp.7z")
        print("decompression zip terminée -> deuxième décompression")
        with py7zr.SevenZipFile(chemin_fichier_7z, mode="r") as z:
            z.extractall(path=dossier_data)

        # suppression des deux fichiers zip:
        os.remove(os.path.join(os.getcwd(), intermediaire_zip))
        os.remove(chemin_fichier_7z)
    else:
        print(f"echec du télechargement code status : {reponse.status_code}")

    # --- suppression des fichiers inutiles de la réunion et de la martinique---
    extensions = ["dbf", "prj", "shp", "shx"]
    for e in extensions:
        try:
            os.remove(os.path.join(dossier_data, f"carreaux_200m_mart.{e}"))
        except Exception:
            print("erreur_suppresion_martinique")
        try:
            os.remove(os.path.join(dossier_data, f"carreaux_200m_reun.{e}"))
        except Exception:
            print("erreur_suppresion_reunion")

    # --- conversion en dataframe centré sur l'idf ---
    df = gpd.read_file(os.path.join(dossier_data, "carreaux_200m_met.shp"))

    # --- récupération des départements associés à lcog_geo ---
    url_base = "https://geo.api.gouv.fr/communes"
    parametres = {
        "codeRegion": "11",              # Île-de-France
        "type": "commune-actuelle,arrondissement-municipal",
        "fields": "nom,code,codeDepartement",  # Les colonnes voulues
        "format": "json"}
    response = requests.get(url_base, params=parametres)
    df2 = pd.DataFrame(response.json())

    # --- rightjoin ---
    df3 = pd.merge(df, df2, left_on="lcog_geo", right_on="code", how="right")
    df3.head()

    # --- récupération des données de pollution ---
    polluants = ["no2", "pm10", "pm25"]
    for p in polluants:
        df3[p] = pd.read_csv(os.path.join(dossier_data, f"donnees_pollution{p}_checkpoint.csv"))

    # --- suppression des données téléchargées ---
    for e in extensions:
        try:
            os.remove(os.path.join(dossier_data, f"carreaux_200m_met.{e}"))
        except Exception:
            print("erreur_suppresion_métropole")
    return (df3)

