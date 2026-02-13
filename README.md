# Python Project – Air Pollution and Living Standards in France

*Authors: Luna Piaraly, Quentin Gouiffes, Lucas Vital*

## Overview

This project was conducted as part of the course **Python for Data Science (2nd year, ENSAE Paris)**. It investigates the relationship between **air pollution** and **living standards** in France using publicly available environmental and socio-economic data aggregated at the municipal level.

The objective is twofold:

- to provide a **descriptive analysis** of the data;
- to conduct a **basic statistical analysis** exploring whether a relationship exists between pollution levels and living conditions.

---

## Research Question

> Is there a statistical relationship between air pollution and living standards across French municipalities?

---

## Data

The project combines:

- **air pollution data** (including PM2.5 concentrations),
- **INSEE socio-economic data** on income and inequality,
- municipal demographic data.

The datasets are cleaned, harmonized, and merged to construct a final analytical dataset.

---

## Notebook Structure

The project is organized into **three notebooks**, to be run in the following order:

1. **`1_data_collection_cleaning.ipynb`**  
   Data collection, cleaning, and preparation of the different datasets.

2. **`2_exploratory_analysis.ipynb`**  
   Descriptive analysis: summary statistics, visualizations, and exploratory plots (Plotly).

3. **`3_modelisation.ipynb`**  
   Statistical analysis: correlations and simple regression models to examine the relationship between pollution and living standards.

---

## Methodology

- Data cleaning and merging
- Univariate and bivariate descriptive analysis
- Data visualization
- Simple statistical modeling and economic interpretation

---

## Reproducibility

- Relative paths from the project root
- Fully commented and independently executable notebooks
- Standard Python dependencies (pandas, numpy, plotly, statsmodels)

---

## Note

This project is exploratory and pedagogical in nature. While it highlights correlations, it does not establish a strict causal relationship.
