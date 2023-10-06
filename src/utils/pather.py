import os


class Pather:
    def __init__(self):
        root_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
            )
        )
        self.raw_data_path = os.path.join(root_path, "data", "raw")
        self.interim_data_path = os.path.join(root_path, "data", "interim")
        self.processed_data_path = os.path.join(root_path, "data", "processed")
        self.reports_path = os.path.join(root_path, "reports")

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
    def interim_accounts(self) -> str:
        return os.path.join(self.interim_data_path, "accounts.csv")

    @property
    def interim_events(self) -> str:
        return os.path.join(self.interim_data_path, "events.csv")

    @property
    def interim_subscriptions(self) -> str:
        return os.path.join(self.interim_data_path, "subscriptions.csv")

    @property
    def interim_users(self) -> str:
        return os.path.join(self.interim_data_path, "users.csv")

    @property
    def features(self) -> str:
        return os.path.join(self.processed_data_path, "features.csv")

    @property
    def target(self) -> str:
        return os.path.join(self.processed_data_path, "target.csv")

    @property
    def eda_report(self) -> str:
        return os.path.join(self.reports_path, "eda_report.html")

    @property
    def features_profile(self) -> str:
        return os.path.join(self.reports_path, "features_profile.html")
