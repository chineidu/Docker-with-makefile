# Docker-with-makefile

This repo shows a simple template for using Docker with a Python app.

It also shows how to build Python packages locally.

## Generating distribution archives

These are archives that are uploaded to the Python Package Index and can be installed by pip.

Make sure you have the latest version of PyPA’s build installed.

```console
# Mac/Linux
$ python3 -m pip install --upgrade build
```

```console
# Windows
$ py -m pip install --upgrade build
```

Now run this command from the same directory where **`pyproject.toml`** is located:

```console
# Mac/Linux
$ python3 -m build
```

```console
# Windows
$ py -m build
```

## Install The Package Locally

```console
$ pip install -e .
```

For more info, check [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
