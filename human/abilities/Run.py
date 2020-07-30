import threading
import random

from human.interface.RunInterface import RunInterface
from human.src.Event import Event

class Run(RunInterface):

    __Name = "[Run.py]"


    def __init__(self):
        print(f"{self.__Name} : init")
        self.__status = False
        self.__steps = 0
        self.__trip = random.randint(1,10)


    def start(self) -> None:
        self.__Thread = threading.Timer(1,self.start)
        self.__Thread.start()
        self.__steps += 1
        self.__status = True
        print(f"[{self.__steps}] : running")

        if self.__steps == self.__trip:
            self.__steps = 0
            self.__trip = random.randint(1,10)
            Event("run","tripped")



    def stop(self) -> bool:
        self.__Thread.join()
        self.__status = False
        return False
    

    def getStatus(self) -> bool:
        return self.__status