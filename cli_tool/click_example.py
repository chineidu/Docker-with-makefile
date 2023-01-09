import click
import os


@click.command()
@click.option("--square", help="calculate the `square` of an integer", type=int)
@click.option("-v", "--verbose", help="increase the verbosity", type=int, default=0)
def func_1(square: int, verbose: int) -> None:
    """CLI tool with verbosity as an input (integer)"""

    result = square**2

    if verbose == 1:
        click.echo(f"square of {square} = {result}")
    elif verbose >= 2:
        click.echo(click.style(f"the square of {square} equals {result}\n", fg="blue"))
    else:
        click.echo(result)


@click.command()
@click.option("-n", "--name", help="enter your name", prompt="your name", required=True)
@click.option("-v", "--verbose", help="increase the verbosity", count=True)
def func_2(name: str, verbose: int) -> None:
    """CLI tool with verbosity as an input (integer)"""

    if verbose == 1:
        click.echo(f"Hello, {name}")
    elif verbose >= 2:
        click.echo(
            click.style(f"Good day {name}. I wish you a productive day", fg="blue")
        )
    else:
        click.echo(f"`{name}`")


PATTERN = os.getenv("PATTERN", "###")


@click.group()
def cli():
    pass


@cli.command()
def load_data() -> None:
    """Used for loading the data."""
    click.echo(f"{PATTERN} Loading the data {PATTERN}")


@cli.command()
def preprocess_data() -> None:
    """Used for preprocessing the data."""
    click.echo(f"{PATTERN} Preprocessing data {PATTERN}")


@cli.command()
def select_features() -> None:
    """Used for loading the data selecting important feature"""
    click.echo(f"{PATTERN} Selecting important features {PATTERN}")


@cli.command()
def train_model() -> None:
    """Used for loading the training the model."""
    click.echo(f"{PATTERN} Training the model {PATTERN}")


if __name__ == "__main__":
    cli()
