# Docker-with-makefile

This repo shows a simple template for using Docker with a Python app.

It also shows how to build Python packages locally.

## Build A Docker Image

```console
docker build -t <tag_name> -f Dockerfile .
```

## Run A Docker Image

```console
docker run -it [-p <port:port>] <tag_name>
```

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
pip install -e .
```

For more info, check [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## AWS CLI

### List Files In An S3 Bucket

```bash
aws s3 ls s3://yourBucketName --recursive --human-readable --summarize
```

### To list only the filenames in a specific folder, add the `--prefix` parameter to the command:

```bash
aws s3api list-objects --bucket YOUR_BUCKET \
    --prefix "my-folder/" --output text \
    --query "Contents[].{Key: Key}"
```

### Upload A File To S3

```bash
aws s3 cp abs_path s3://yourBucketName/
```

### Uploading Multiple Files and Folders to S3 Recursively

```bash
aws s3 cp abs_path s3://yourBucketName/ --recursive
```

### Download a file from S3

```bash
aws s3 cp s3://yourBucketName abs_path

```

### Download Multiple Files From S3

```bash
aws s3 cp s3://yourBucketName abs_path --recursive

```
