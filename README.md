# jktech-accelerators-deploy

Shared CI workflows for the JK Tech accelerators. Product source stays in each private repository. This repository stores the pipeline and the settings for that repository.

A teammate opens the accelerator they were given. That repository calls one shared workflow and names itself. This repository then loads `accelerators/<name>/config.yml` and runs the commands in that file.

Every repository and its assigned workflow is listed in [CATALOG.md](CATALOG.md). A row without a config file does not have a running pipeline yet. Install, lint, and test commands stay in that repository's `config.yml`.

## Caller in the private repository

The private repository keeps only this caller. The steps stay here.

```yaml
name: ci

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  ci:
    uses: jktech-dev-accelrators/jktech-accelerators-deploy/.github/workflows/<workflow>.yml@main
    with:
      accelerator: <repository-name>
```

`<workflow>` is the value from [CATALOG.md](CATALOG.md): `library`, `service`, `web`, `data-pipeline`, or `tool`. `<repository-name>` is the accelerator folder under `accelerators/`.

The shared workflow checks out that private repository, reads its config from `main` of this repository, and runs the commands in the config. Push this repository before the caller can succeed.

## Add the next accelerator

1. Confirm the workflow in [CATALOG.md](CATALOG.md).
2. Add `accelerators/<repository>/config.yml` when that runtime is implemented. `name` must match the folder. `install`, `lint`, and `test` are the commands for that repository.
3. Point the private caller at the matching shared workflow.

`library` for Python is the implemented pair today. `service`, `web`, `data-pipeline`, and `tool` are added with the first repository of that kind.
