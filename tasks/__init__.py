from invoke import task


@task()
def create_dataset(ctx, wait=True):
    ctx.run(f"python -m src.data.make_dataset", echo=True)


@task()
def create_eda_report(ctx, wait=True):
    ctx.run(f"python -m python -m src.visualization.eda", echo=True)
