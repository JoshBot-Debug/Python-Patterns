from human.interface.GenderInterface import GenderInterface
from human.interface.MaleInterface import MaleInterface

class Gender(GenderInterface,MaleInterface):
    """
        Type: Male
    """

    __Name = "[male\\Gender.py]"

    def __init__(self):
        print(f"{self.__Name} : init")

    
    def gender(self):
        return "male"