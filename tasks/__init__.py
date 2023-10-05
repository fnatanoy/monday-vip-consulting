from invoke import task


@task()
def make_interim_dataset(ctx, wait=True):
    ctx.run(f"python -m src.data.make_interim_dataset", echo=True)


@task()
def create_eda_report(ctx, wait=True):
    ctx.run(f"python -m python -m src.visualization.eda", echo=True)
