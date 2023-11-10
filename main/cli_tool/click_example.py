import os

import click


@click.command()
@click.option("--square", help="calculate the `square` of an integer", type=int)
@click.option("-v", "--verbose", help="increase the verbosity", type=int, default=0)
def func_1(square: int, verbose: int) -> None:  # pylint: disable=useless-return
    """CLI tool with verbosity as an input (integer)

    Params:
        square (int): The number to square
        verbose (int, default=0): The level of verbosity. The greater the number,
                                the greater the verbosity.

    Returns:
        None: None
    """

    result = square**2

    if verbose == 1:
        click.echo(f"square of {square} = {result}")
    elif verbose >= 2:
        click.echo(click.style(f"the square of {square} equals {result}\n", fg="blue"))
    else:
        click.echo(result)
    return None


@click.command()
@click.option("-n", "--name", help="enter your name", prompt="your name", required=True)
@click.option("-v", "--verbose", help="increase the verbosity", count=True)
def func_2(name: str, verbose: str) -> None:  # pylint: disable=useless-return
    """CLI tool with verbosity as an input (integer)

    Params:
        square (int): The number to square
        verbose (str, default=0): The level of verbosity. The greater the number,
                                    the greater the verbosity.

    Returns:
        None : None
    """

    if verbose == 1:
        click.echo(f"Hello, {name}")
    elif verbose >= 2:  # type: ignore[operator]
        click.echo(click.style(f"Good day {name}. I wish you a productive day", fg="blue"))
    else:
        click.echo(f"`{name}`")

    return None


PATTERN = os.getenv("PATTERN", "###")


@click.group()
def cli():
    """Cmd"""
    pass  # pylint: disable=unnecessary-pass


@cli.command()
def load_data() -> None:  # pylint: disable=useless-return
    """Used for loading the data."""
    click.echo(f"{PATTERN} Loading the data {PATTERN}")
    return None


@cli.command()
def preprocess_data() -> None:  # pylint: disable=useless-return
    """Used for preprocessing the data."""
    click.echo(f"{PATTERN} Preprocessing data {PATTERN}")
    return None


@cli.command()
def select_features() -> None:  # pylint: disable=useless-return
    """Used for loading the data selecting important feature"""
    click.echo(f"{PATTERN} Selecting important features {PATTERN}")
    return None


@cli.command()
def train_model() -> None:  # pylint: disable=useless-return
    """Used for loading the training the model."""
    click.echo(f"{PATTERN} Training the model {PATTERN}")
    return None


if __name__ == "__main__":
    cli()
