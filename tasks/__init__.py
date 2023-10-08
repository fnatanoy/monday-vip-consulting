from invoke import task


@task()
def make_interim_dataset(ctx, wait=True):
    ctx.run(f"python -m src.data.make_interim_dataset", echo=True)


@task()
def make_features(ctx, wait=True):
    ctx.run(f"python -m src.data.make_features_dataset", echo=True)


@task()
def create_eda_report(ctx, wait=True):
    ctx.run(f"python -m src.visualization.eda", echo=True)


@task()
def create_features_profiling(ctx, wait=True):
    ctx.run(f"python -m src.visualization.features_profiling", echo=True)


@task()
def train_logistic(ctx, wait=True):
    ctx.run(f"python -m src.models.logistic_regression", echo=True)


@task()
def train_xgboost(ctx, train_mode, wait=True):
    print(train_mode)
    ctx.run(f"python -m src.models.xgboost -m {train_mode}", echo=True)
