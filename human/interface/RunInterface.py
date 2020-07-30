import abc

class RunInterface(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def start(self) -> None: pass


    @abc.abstractmethod
    def stop(self) -> bool: pass


    @abc.abstractmethod
    def getStatus(self) -> bool: pass