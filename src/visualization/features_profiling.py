import pandas as pd
from src.utils.pather import Pather
from ydata_profiling import ProfileReport


def profile():
    pather = Pather()
    features = pd.read_csv(pather.features).set_index("account_id")
    target = pd.read_csv(pather.target).set_index("account_id")
    data = features.merge(target, left_index=True, right_index=True)

    profile = ProfileReport(data, title="Monday VIP CONSULTING")
    profile.to_file(pather.features_profile)


"""
python -m src.visualization.features_profiling
"""
if __name__ == "__main__":
    profile()
