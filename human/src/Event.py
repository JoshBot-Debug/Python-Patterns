from human.src.Observer import Observer

class Event(object):


    __Name = "[Event.py]"


    def __init__(self,Key: str, Data, Fire = True):
        print(f"{self.__Name} : init")

        self.__key = Key
        self.__data = Data
        if Fire:
            self.__Fire()


    def __Fire(self) -> bool:
        
        for observer in Observer._observers:
                if self.__key in observer._observables:
                    observer._observables[self.__key](self.__data)
                    return True
        
        raise Exception("Invalid Key")