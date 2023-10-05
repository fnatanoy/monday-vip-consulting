import pandas as pd
from src.utils.pather import Pather


class Dataset:
    NANS_THRESHOLD = 0.8

    def __init__(self) -> None:
        self.pather = Pather()
        print("Loading Data...")
        self.accounts = pd.read_csv(self.pather.raw_accounts)
        self.users = pd.read_csv(self.pather.raw_users)
        self.events = pd.read_csv(self.pather.raw_events)
        self.subscriptions = pd.read_csv(self.pather.raw_subscriptions)

    def create_interim_dataset(self) -> None:
        self._remove_with_non_indicative_account_id_and_add_label()
        self._remove_unnecessary_columns()
        self._save_dataset()

    def _remove_with_non_indicative_account_id_and_add_label(self) -> None:
        self.subscriptions = self.subscriptions.merge(
            self.accounts[["account_id", "plan_id", "lead_score"]],
            on=["account_id", "plan_id"],
            how="inner",
        )
        self.users = self.users.merge(
            self.accounts[["account_id", "lead_score"]],
            on=["account_id"],
            how="inner",
        )
        self.events = self.events.merge(
            self.accounts[["account_id", "lead_score"]],
            on=["account_id"],
            how="inner",
        )

    def _remove_unnecessary_columns(self) -> None:
        print(
            f"Removing columns with more then {100 *(1-self.NANS_THRESHOLD)}% NaNs..."
        )
        self.clean_accounts = self.accounts.dropna(
            axis=1, thresh=len(self.accounts) * self.NANS_THRESHOLD
        )
        self.clean_accounts = self.clean_accounts.join(self.accounts["plan_id"].copy())
        # self.clean_accounts = self.clean_accounts.dropna(
        #     subset=["lead_score"]
        # ).reset_index(drop=True)

        self.clean_users = self.users.dropna(
            axis=1, thresh=len(self.users) * self.NANS_THRESHOLD
        )
        self.clean_events = self.events.dropna(
            axis=1, thresh=len(self.events) * self.NANS_THRESHOLD
        )
        self.clean_subscriptions = self.subscriptions.dropna(
            axis=1, thresh=len(self.subscriptions) * self.NANS_THRESHOLD
        )
        print(
            f"removed {len(self.accounts.columns) - len(self.clean_accounts.columns)} columns from accounts"
        )
        print(
            f"removed {len(self.users.columns) - len(self.clean_users.columns)} columns from users"
        )
        print(
            f"removed {len(self.events.columns) - len(self.clean_events.columns)} columns from events"
        )
        print(
            f"removed {len(self.subscriptions.columns) - len(self.clean_subscriptions.columns)} columns from subscriptions"
        )

    def _save_dataset(self) -> None:
        print("Saving dataset...")
        self.clean_accounts.to_csv(self.pather.interim_accounts, index=False)
        self.clean_users.to_csv(self.pather.interim_users, index=False)
        self.clean_events.to_csv(self.pather.interim_events, index=False)
        self.clean_subscriptions.to_csv(self.pather.interim_subscriptions, index=False)


"""
python -m src.data.make_dataset
"""
if __name__ == "__main__":
    dataset = Dataset()
    dataset.create_interim_dataset()
    # dataset.create_features()
