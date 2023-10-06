import pandas as pd
from src.utils.pather import Pather


class FeaturesDataset:
    def __init__(self) -> None:
        self.pather = Pather()
        print("Loading Data...")
        self.accounts = pd.read_csv(self.pather.interim_accounts)
        self.users = pd.read_csv(self.pather.interim_users)
        self.events = pd.read_csv(self.pather.interim_events)

    def create_features(self) -> None:
        accounts_features = self._create_accounts_features()
        events_features = self._create_events_features()
        users_features = self._create_users_features()

        features = accounts_features.merge(
            users_features,
            left_index=True,
            right_index=True,
            how="outer",
        ).merge(
            events_features,
            left_index=True,
            right_index=True,
            how="outer",
        )
        target = features.pop("lead_score")
        self._save_dataset(features, target)

    def _create_users_features(self) -> pd.DataFrame:
        return (
            self.users.groupby("account_id")
            .agg(
                {
                    "user_id": "nunique",
                    "is_admin": "sum",
                    "pending": "sum",
                    "enabled": "sum",
                }
            )
            .rename(
                columns={
                    "user_id": "registered_users",
                    "is_admin": "number_of_admins",
                    "pending": "number_of_pending_users",
                    "enabled": "number_of_enabled_users",
                }
            )
        )

    def _create_accounts_features(self) -> pd.DataFrame:
        features = [
            "account_id",
            "paying",
            "collection_21_days",
            "max_team_size",
            "min_team_size",
            "industry",
            "payment_currency",
            # "region",
            # "country",
            "lead_score",
        ]
        return (
            self.accounts[features]
            .copy()
            .set_index("account_id")
            .astype(
                {
                    "industry": "category",
                    "payment_currency": "category",
                    # "region": "category",
                    # "country": "category",
                }
            )
        )

    def _create_events_features(self) -> pd.DataFrame:
        return (
            self.events.groupby(["account_id"])
            .agg(
                dict(
                    user_id="nunique",
                    date="nunique",
                    total_events="sum",
                    column_events="sum",
                    board_events="sum",
                    num_of_boards="sum",
                    count_kind_columns="sum",
                    content_events="sum",
                    group_events="sum",
                    invite_events="sum",
                    import_events="sum",
                    notification_events="sum",
                    new_entry_events="sum",
                    payment_events="sum",
                    inbox_events="sum",
                    communicating_events="sum",
                    non_communicating_events="sum",
                    web_events="sum",
                    ios_events="sum",
                    android_events="sum",
                    desktop_app_events="sum",
                    empty_events="sum",
                )
            )
            .rename(columns={"user_id": "active_of_users", "date": "active_days"})
            .query("total_events > 0")
        )

    def _save_dataset(self, features, target) -> None:
        print("Saving dataset...")
        features.to_csv(self.pather.features, index=True)
        target.to_csv(self.pather.target, index=True)


"""
python -m src.data.make_features_dataset
"""
if __name__ == "__main__":
    dataset = FeaturesDataset()
    dataset.create_features()
