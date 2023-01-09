# Development Using Docker

* Project structure

```console
.
├── README.md
├── environment
│   └── Dockerfile
├── file.py
└── simple_app
    ├── __init__.py
    ├── app.py
    └── data
        └── target.csv
```

## Dockerfile

```dockerfile
FROM python:3.10-slim

RUN pip3 install --upgrade --no-cache pandas \
    scikit-learn numpy click

```
> I kept the dockerfile very simple to avoid building a bloated image. The dockerfile was also kept in the directory `environment` so that only the file in the directory is included the image.
The other files will be mounted to prevent `re-building` of the image whenever changes are made to the code.

* To build the image, run:

```console
docker build -t tutorial:v1 /environment/Dockerfile .
```

## Python Code (app.py)

```python
import click
import numpy as np
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
```

* To run the python script, run:

```console
docker run --rm \
    --mount type=bind,source="${PWD}/simple_app",target=/mnt \
    --workdir /mnt \
    tutorial:v1 \
    python app.py --filepath "./data/target.csv"
```

* The output:

```text
Loading data ...
Making predictions ...
                                     id     target  prediction
0  dc3841e4-4dc2-44e5-befa-75f415c7ddc7   8.400000      7.9632
1  b9242daf-a7b9-47e2-a4e3-06e2a75e913b   8.966667      8.5004
2  ece22dfd-24cb-4f73-8e64-74309ec1f145  10.033333      9.5116
3  e33203f5-9172-489b-8c6f-9b1716ddcf17  37.533333     35.5816
4  737bff44-4cba-4731-b8a0-7701bc04b364  29.550000     28.0134
```