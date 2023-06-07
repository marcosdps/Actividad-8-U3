from zope.interface import Interface



class Iagente(Interface): 
    def insertarElemento(self, posicion, agente):
        pass
    def agregarElemento(self, agente):
        pass
    def mostrarElemento(self, posicion):
        pass
