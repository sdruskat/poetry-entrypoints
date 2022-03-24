from abc import ABC, abstractmethod


class AbstractPlugin(ABC):

    @staticmethod
    @abstractmethod
    def run():
        pass
