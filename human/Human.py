from human.src.Observer import Observer

from human.interface.MaleInterface import MaleInterface
from human.interface.FemaleInterface import FemaleInterface
from human.interface.GenderInterface import GenderInterface
from human.interface.RunInterface import RunInterface


class Human(object):
    """
        The base character, accepts a GenderInterface on init
    """

    __Name = "[Human.py]"
    __Gender: str = ""
    __Ability: dict = {}


    def __init__(self,GenderInterface: GenderInterface):
        print(f"{self.__Name} : init")

        # Init the Observer() and set it
        Observer().setObservable("run",self.runEvents)

        if isinstance(GenderInterface,MaleInterface):
            print(f"{self.__Name} : I am a man")

        if isinstance(GenderInterface,FemaleInterface):
            print(f"{self.__Name} : I am a Female")

        self.__Gender = GenderInterface.gender()

        


    def getAttributes(self) -> list:
        return [
            self.__Gender,
        ]


    def run(self, Ri: RunInterface) -> None:

        if not isinstance(Ri,RunInterface):
            raise Exception("The class has to belong to the RunInterface")

        if "run" not in self.__Ability:
            self.__Ability.update({"run":Ri})
        
        self.__Ability["run"].start()


    def runEvents(self,Data) -> str:
        print(f"[runEvents()] {Data}")
        return Data