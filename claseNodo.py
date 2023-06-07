from clasePersonal import Personal

class Nodo:
    __agente: Personal
    __siguiente: object

    def __init__(self, agente=None) -> None:
        self.__agente = agente
        self.__siguiente = None

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__agente
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente