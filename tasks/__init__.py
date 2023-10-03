from invoke import task


@task()
def create_dataset(ctx, wait=True):
    ctx.run(f"python -m src.data.make_dataset", echo=True)
