import pandas as pd
from src.utils.pather import Pather
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


class RandomForest:
    @classmethod
    def train(cls):
        pather = Pather()
        features = pd.read_csv(pather.features).set_index("account_id")
        categorical_cols = ["payment_currency", "industry"]
        one_hot_encoder = OneHotEncoder(sparse=False, drop="first")
        preprocessor = ColumnTransformer(
            transformers=[("cat", one_hot_encoder, categorical_cols)],
            remainder="passthrough",
        )
        X_encoded = preprocessor.fit_transform(features)
        y = pd.read_csv(pather.target).set_index("account_id")["lead_score"].values

        X_train, X_val_test, y_train, y_val_test = train_test_split(
            X_encoded, y, test_size=0.3, random_state=42
        )
        X_val, X_test, y_val, y_test = train_test_split(
            X_val_test, y_val_test, test_size=0.5, random_state=42
        )
        import ipdb; ipdb.set_trace()  # fmt: skip
        rf_classifier = RandomForestClassifier(
            n_estimators=10,
            random_state=42,
            max_depth=10,
            class_weight="balanced_subsample",
            verbose=True,
        )
        y_train_pred = rf_classifier.predict(X_train)
        y_val_pred = rf_classifier.predict(X_val)
        y_test_pred = rf_classifier.predict(X_test)

        train_precision = precision_score(y_train, y_train_pred)
        val_precision = precision_score(y_val, y_val_pred)
        test_precision = precision_score(y_test, y_test_pred)

        # for train_idx, test_idx in stratified_kfold.split(X_encoded, target):
        #     X_train, X_test = X_encoded[train_idx, :], X_encoded[test_idx, :]
        #     y_train, y_test = target[train_idx], target[test_idx]

        #     rf_classifier.fit(X_train, y_train)
        #     import ipdb; ipdb.set_trace()  # fmt: skip

        #     # precision_scores.append(precision_score(y_test, y_pred))
        #     # f1_scores.append(f1_score(y_test, y_pred))

        # mean_f1_score = sum(f1_scores) / len(f1_scores)

        # print(f"Mean F1 Score: {mean_f1_score:.2f}")


"""
python -m src.models.random_forest
"""
if __name__ == "__main__":
    RandomForest.train()
