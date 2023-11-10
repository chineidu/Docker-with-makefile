# CLI Usage

```python
import click
import os

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
    click.echo("Preprocessing data ...")


@cli.command()
def select_features() -> None:
    """Used for loading the data selecting important feature"""
    click.echo("Selecting important features ...")


@cli.command()
def train_model() -> None:
    """Used for loading the training the model."""
    click.echo("Training the model ...")


if __name__ == "__main__":
    cli()
```

> To use, run:

```console
python cli_tool/click_example.py load-data
```

* Result

```text
### Load the data ###
```

> To use, run:

```console
PATTERN="..."
python cli_tool/click_example.py train-model
```

* Result

```text
... Training the model ...
```
