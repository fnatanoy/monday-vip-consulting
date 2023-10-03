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

    def create_dataset(self) -> None:
        self._remove_unnecessary_columns()
        self._save_dataset()

    def _remove_unnecessary_columns(self) -> None:
        print(f"Removing columns with more then {100 *self.NANS_THRESHOLD}% NaNs...")
        self.clean_accounts = self.accounts.dropna(
            axis=1, thresh=len(self.accounts) * self.NANS_THRESHOLD
        )
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
        self.clean_accounts.to_csv(self.pather.processed_accounts, index=False)
        self.clean_users.to_csv(self.pather.processed_users, index=False)
        self.clean_events.to_csv(self.pather.processed_events, index=False)
        self.clean_subscriptions.to_csv(
            self.pather.processed_subscriptions, index=False
        )


"""
python -m src.data.make_dataset
"""
if __name__ == "__main__":
    dataset = Dataset()
    dataset.create_dataset()
