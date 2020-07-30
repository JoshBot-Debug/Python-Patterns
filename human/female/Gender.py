from human.interface.GenderInterface import GenderInterface
from human.interface.FemaleInterface import FemaleInterface

class Gender(GenderInterface,FemaleInterface):
    """
        Type: Female
    """

    __Name = "[female\\Gender.py]"


    def __init__(self):
        print(f"{self.__Name} : init")


    def gender(self):
        return "female"