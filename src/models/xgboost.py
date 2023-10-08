import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from skopt import BayesSearchCV
from src.utils.pather import Pather
from skopt.space import Integer


def train(params: dict = {}):
    learning_rate = params.get("learning_rate", 0.1)
    n_estimators = params.get("n_estimators", 20)
    max_depth = params.get("max_depth", 20)
    min_child_weight = params.get("min_child_weight", 1)

    X_train, X_test, y_train, y_test = get_xy()
    model = xgb.XGBClassifier(
        learning_rate=learning_rate,
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_child_weight=min_child_weight,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        seed=42,
        enable_categorical=True,
        max_cat_to_onehot=5,
    )
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_f1 = f1_score(y_train, y_train_pred)
    test_f1 = f1_score(y_test, y_test_pred)
    print(f"Train f1 score: {train_f1}")
    print(f"Test f1 score: {test_f1}")

    train_precision = precision_score(y_train, y_train_pred)
    test_precision = precision_score(y_test, y_test_pred)
    print(f"Train precision score: {train_precision}")
    print(f"Test precision score: {test_precision}")

    train_recall = recall_score(y_train, y_train_pred)
    test_recall = recall_score(y_test, y_test_pred)
    print(f"Train recall score: {train_recall}")
    print(f"Test recall score: {test_recall}")


def hyperparameter_search():
    X_train, _, y_train, _ = get_xy()
    param_space = {
        "learning_rate": (0.1, 0.3, "log-uniform"),
        "n_estimators": Integer(20, 300),
        "max_depth": Integer(5, 100),
        "min_child_weight": Integer(1, 3),
    }

    xgb_classifier = xgb.XGBClassifier(
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        seed=42,
        enable_categorical=True,
        max_cat_to_onehot=5,
    )
    bayes_search = BayesSearchCV(
        xgb_classifier,
        param_space,
        n_iter=100,
        cv=5,
        scoring="f1",
        n_jobs=-1,
        verbose=0,
    )
    bayes_search.fit(X_train, y_train)

    best_params = bayes_search.best_params_
    print(best_params)


def get_xy():
    pather = Pather()
    features = pd.read_csv(pather.features).set_index("account_id")
    y = pd.read_csv(pather.target).set_index("account_id")["lead_score"].values
    features = features.astype(
        {
            "payment_currency": "category",
            "industry": "category",
            "country": "category",
        }
    )
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        y,
        stratify=y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    # train()
    best_params = dict(
        learning_rate=0.3,
        n_estimators=300,
        max_depth=5,
        min_child_weight=1,
    )
    hyperparameter_search(best_params)
