from entrypoints.plugins.abc import AbstractPlugin


class Plugin(AbstractPlugin):

    @staticmethod
    def run():
        print(f'Running from {Plugin.__module__}')
