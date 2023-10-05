import pandas as pd
from src.utils.pather import Pather


class InterimDataset:
    NANS_THRESHOLD = 0.5

    def __init__(self) -> None:
        self.pather = Pather()
        print("Loading Data...")
        self.accounts = pd.read_csv(self.pather.raw_accounts)
        self.users = pd.read_csv(self.pather.raw_users)
        self.events = pd.read_csv(self.pather.raw_events)
        self.subscriptions = pd.read_csv(self.pather.raw_subscriptions)

    def create_interim_dataset(self) -> None:
        self._remove_duplicate_rows()
        self._remove_rows_with_non_indicative_account_id_and_add_label()
        self._remove_unnecessary_columns()
        self._save_dataset()

    def _remove_rows_with_non_indicative_account_id_and_add_label(self) -> None:
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

    def _remove_duplicate_rows(self) -> None:
        # self.users.groupby(by=["account_id", "user_id"]).size().reset_index().sort_values(by=0, ascending=False)
        # self.users[(self.users["account_id"] == 319758) & (self.users["user_id"] == 515534)
        self.users = self.users.drop_duplicates(
            subset=["account_id", "user_id"], keep="first"
        )

        # self.accounts.groupby(by=["account_id"]).size().reset_index().sort_values(
        #     by=0, ascending=False
        # )
        # self.accounts[(self.accounts["account_id"] == 933422)]
        self.accounts = self.accounts.drop_duplicates(
            subset=["account_id"], keep="first"
        )

        self.subscriptions = self.subscriptions.drop_duplicates(keep="first")

        # self.events.groupby(
        #     by=["date", "user_id", "account_id"]
        # ).size().reset_index().sort_values(by=0, ascending=False)
        self.events = self.events.drop_duplicates(keep="first")

    def _remove_unnecessary_columns(self) -> None:
        print(
            f"Removing columns with more then {round(100 *(1-self.NANS_THRESHOLD),1)}% NaNs..."
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
            f"removed {set(self.accounts.columns) - set(self.clean_accounts.columns)} from accounts"
        )
        print(
            f"removed {set(self.users.columns) - set(self.clean_users.columns)} from users"
        )
        print(
            f"removed {set(self.events.columns) - set(self.clean_events.columns)} from events"
        )
        print(
            f"removed {set(self.subscriptions.columns) - set(self.clean_subscriptions.columns)} from subscriptions"
        )

    def _save_dataset(self) -> None:
        print("Saving dataset...")
        self.clean_accounts.to_csv(self.pather.interim_accounts, index=False)
        self.clean_users.to_csv(self.pather.interim_users, index=False)
        self.clean_events.to_csv(self.pather.interim_events, index=False)
        self.clean_subscriptions.to_csv(self.pather.interim_subscriptions, index=False)


"""
python -m src.data.make_interim_dataset
"""
if __name__ == "__main__":
    dataset = InterimDataset()
    dataset.create_interim_dataset()
