import pandas as pd
from reportity import reportity
import plotly.graph_objects as go

from src.utils.pather import Pather


class EDA:
    def __init__(self) -> None:
        self.pather = Pather()
        self.accounts = pd.read_csv(self.pather.processed_accounts)
        self.users = pd.read_csv(self.pather.processed_users)
        # self.events = pd.read_csv(self.pather.processed_events)
        self.subscriptions = pd.read_csv(self.pather.processed_subscriptions)

        self.report = reportity.Reportity("Monday VIP CONSULTING")

    def analyze(self) -> None:
        self._analyze_accounts_users()
        # self._analyze_subscriptions()
        # self._plot_events()
        # self._plot_users()
        # self._plot_subscriptions()

        self.report.save_as_html(self.pather.eda_report)
        self.report.show()

    # def _analyze_subscriptions(self) -> None:
    #     # import ipdb; ipdb.set_trace()  # fmt: skip
    #     # subscriptions = self.subscriptions.merge(
    #     #     self.accounts, on=["account_id", "plan_id"], how="inner"
    #     # )

    def _analyze_accounts_users(self) -> None:
        number_of_accounts = len(self.accounts["account_id"].unique())
        vip_clients = sum(self.accounts["lead_score"] == 1)
        non_vip_clients = sum(self.accounts["lead_score"] == 0)

        users_per_account = self.users.groupby("account_id")["user_id"].count()

        self.report.print_header("Accounts", level=1)
        self.report.print_paragraph(f"Number of accounts: {number_of_accounts:,}")
        self.report.print_paragraph(f"VIP clients: {vip_clients:,}")
        self.report.print_paragraph(f"Non-VIP clients: {non_vip_clients:,}")
        self.report.print_paragraph(
            f"VIP/Non-VIP ratio: {round(vip_clients/non_vip_clients, 4)}"
        )

        self.report.print_figure(
            go.Figure()
            .add_trace(go.Histogram(x=users_per_account))
            .update_layout(
                title="Users Per Account",
                xaxis_title="Users",
                yaxis_title="# of Accounts",
                font={"size": 18},
            )
        )


"""
python -m src.visualization.eda
"""
if __name__ == "__main__":
    eda = EDA()
    eda.analyze()
