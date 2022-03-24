# Poetry entrypoints

This is an example project that uses [`poetry`](https://python-poetry.org/) `plugins` to provide plugins to a simple [`typer`](https://typer.tiangolo.com/) Python app.

Two plugins are defined in [`pyproject.toml`](pyproject.toml) as follows:

```toml
[tool.poetry.plugins."entrypoints.plugins"]
plugin1 = "entrypoints.plugins.plugin1:Plugin"
plugin2 = "entrypoints.plugins.plugin2:Plugin"
```

Their implementation is in the Python modules `entrypoints/plugins/plugin\<n\>`, 
in the form of classes implementing the abstract plugin class `entrypoints.plugins.abc.AbstractPlugin`.

The abstract class defines one static method `run()`, which must also be implemented in the subclasses.

Finally, everything is knit together in `entrypoints/__main__.py`, which calls a typer method `run()` 
that retrieves the defined entrypoints in in `'entrypoints.plugins'` namespace, 
and calls the respective plugin `run()` method iteratively for each discovered entrypoint.

## Usage

Clone this repository, then use poetry to install the package `entrypoints`, and finally run it.

```bash
git clone git@github.com:sdruskat/poetry-entrypoints.git
cd poetry-entrypoints
poetry shell
poetry install
python -m entrypoints
```

## Development

If you want to play around with further plugins, make sure to run `poetry install` when you change entrypoint/plugin definitions, otherwise they won't be discoverable.

## License

This README is public domain-like under [CC0](https://creativecommons.org/publicdomain/zero/1.0/legalcode).
The code is licensed under [MIT](LICENSE).
