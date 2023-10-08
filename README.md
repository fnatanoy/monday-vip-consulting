# monday-vip-consulting

## Project Description

## Project Installation

1. Install all requirements

    ```bash
    pip install -r requirements.txt
    ```

2. Install pre-commit hooks

    ```bash
    pre-commit install
    ```

3. Add all 4 data csvs to `data/raw` folder

## Create Datasets

1. Create intermediate dataset

    ```bash
    inv make_interim_dataset
    ```

2. Create Features

    ```bash
    inv make_features
    ```

## EDA

1. Run the following command to generate the EDA report

    ```bash
    inv create_eda_report
    ```

2. Create profiler for the features

    ```bash
    inv create_features_profiling
    ```

## Model Training

1. Logistic regression:

    ```bash
    inv train_logistic
    ```

2. XGBoost:

    ```bash
    inv train_xgboost -train-mode train
    ```

## Project Organization

------------
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │ 
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented 
    │
    └──

--------

Project based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/) #cookiecutterdatascience

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
