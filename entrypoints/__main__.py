import typer
import importlib.metadata


def run():
    print(f'Hello from run.')
    for ep in importlib.metadata.entry_points()['entrypoints.plugins']:
        datasource = ep.load()
        datasource.run()


if __name__ == '__main__':
    print('Hello from __main__.')
    typer.run(run)