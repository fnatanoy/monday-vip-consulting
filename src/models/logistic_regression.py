import pandas as pd
from src.utils.pather import Pather
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn import preprocessing


def train():
    pather = Pather()
    features = pd.read_csv(pather.features).set_index("account_id")
    y = pd.read_csv(pather.target).set_index("account_id")["lead_score"].values
    categorical_cols = ["payment_currency", "industry", "country"]
    features = features.drop(categorical_cols, axis=1)

    X = features.values
    scaler = preprocessing.StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )
    model = LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42,
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


if __name__ == "__main__":
    train()
