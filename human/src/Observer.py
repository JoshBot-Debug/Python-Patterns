
class Observer(object):


    __Name = "[Observer.py]"
    _observers = []

    def __init__(self):
        print(f"{self.__Name} : init")
        self._observers.append(self)
        self._observables = {}


    def setObservable(self,Key: str, Func) -> None:
        if Key not in self._observables:
            self._observables.update({Key:Func})


    def removeObservable(self,Key: str) -> None:
        if Key in self._observables:
            self._observables.pop(Key)