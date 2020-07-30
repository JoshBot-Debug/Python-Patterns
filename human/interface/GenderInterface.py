import abc

class GenderInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def gender(self) -> str: pass