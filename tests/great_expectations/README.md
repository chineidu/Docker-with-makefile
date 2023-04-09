# Great  Expectations Projects

## Table of Contents

- [Great  Expectations Projects](#great--expectations-projects)
  - [Table of Contents](#table-of-contents)
  - [Initialize Project](#initialize-project)
  - [Common Commands](#common-commands)
  - [Connect Data Source](#connect-data-source)
  - [Check Points](#check-points)
  - [Documentation](#documentation)

## Initialize Project

```bash
great_expectations init
```

> The `tests/great_expectations` directory will be created with the following structure:

```text
    great_expectations
    |-- great_expectations.yml
    |-- expectations
    |-- checkpoints
    |-- plugins
    |-- .gitignore
    |-- uncommitted
        |-- config_variables.yml
        |-- data_docs
        |-- validations
```

## Common Commands

```text
  Use the CLI to:
- Run `great_expectations datasource new` to connect to your data.
- Run `great_expectations checkpoint new <checkpoint_name>` to bundle data with Expectation Suite(s) in a Checkpoint for later re-validation.
- Run `great_expectations suite --help` to create, edit, list, profile Expectation Suites.
- Run `great_expectations docs --help` to build and manage Data Docs sites.
```

## Connect Data Source

> The first step is to set up our datasource, which informs Great Expectations about the location of our data:

```bash
great_expectations datasource new
```

> Select: **`Files on a filesystem (for processing with Pandas or Spark) 👈`**

## Check Points

> Establish checkpoints where a set of expectations is applied to a particular data asset. This is an excellent way to programmatically apply checkpoints to our new and existing data sources.

```bash
cd tests
great_expectations checkpoint new CHECKPOINT_NAME
```

- An example would be:

```bash
great_expectations checkpoint new salary_data
```

> This opens a Jupyter notebook with the following:

```text
my_checkpoint_name = "salary_data"  # This was populated from your CLI command.

yaml_config = f"""
name: {my_checkpoint_name}
config_version: 1.0
class_name: SimpleCheckpoint
run_name_template: "%Y%m%d-%H%M%S-my-run-name-template"
validations:
  - batch_request:
      datasource_name: my_datasource
      data_connector_name: default_inferred_data_connector_name
      data_asset_name: salary.csv # Ensure that this is correct!
      data_connector_query:
        index: -1
    expectation_suite_name: salary_suite  # Ensure that this is correct!
"""
```

- Ensure that the **`data_asset_name`**  and **`expectation_suite_name`** are correct!
- Execute the checkpoint by running:

```bash
great_expectations checkpoint run <checkpoint_name>

# e.g
great_expectations checkpoint run salary_data
```

## Documentation

> Great Expectations automatically provides `test documentation` when we set expectations using the CLI tool. Additionally, it keeps track of validation attempts and their outcomes.

```bash
great_expectations docs build
```
