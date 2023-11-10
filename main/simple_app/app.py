import click
import pandas as pd


@click.command()
@click.option("-f", "--filepath", help="The filepath", type=str)
@click.option("-n", "--num", help="The number of rows", default=5)
def load_data(filepath: str, num: int) -> pd.DataFrame:
    """This is used to load the data."""
    print(click.style("\nLoading data ...", fg="yellow"))
    df = pd.read_csv(filepath).iloc[:num]
    columns = ["id", "target"]
    df.columns = columns

    print(click.style("Making predictions ...", fg="yellow"))
    df = df.assign(prediction=lambda x: x["target"] * 0.948)
    click.echo(df)
    return df


if __name__ == "__main__":
    load_data()
