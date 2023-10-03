import os


class Pather:
    def __init__(self):
        data_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "data",
            )
        )
        self.raw_data_path = os.path.join(data_path, "raw")
        self.processed_data_path = os.path.join(data_path, "processed")

    @property
    def raw_accounts(self) -> str:
        return os.path.join(self.raw_data_path, "accounts.csv")

    @property
    def raw_events(self) -> str:
        return os.path.join(self.raw_data_path, "events.csv")

    @property
    def raw_subscriptions(self) -> str:
        return os.path.join(self.raw_data_path, "subscriptions.csv")

    @property
    def raw_users(self) -> str:
        return os.path.join(self.raw_data_path, "users.csv")

    @property
    def processed_accounts(self) -> str:
        return os.path.join(self.processed_data_path, "accounts.csv")

    @property
    def processed_events(self) -> str:
        return os.path.join(self.processed_data_path, "events.csv")

    @property
    def processed_subscriptions(self) -> str:
        return os.path.join(self.processed_data_path, "subscriptions.csv")

    @property
    def processed_users(self) -> str:
        return os.path.join(self.processed_data_path, "users.csv")
