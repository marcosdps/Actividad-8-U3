from claseNodo import Nodo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseApoyo import PersonalApoyo
from claseNodo import Nodo
from zope.interface import implementer
from claseInterfaz import Iagente
from interfaceDirector import Idirector
from interfaceTesorero import Itesorero


@implementer(Idirector)
@implementer(Itesorero)
@implementer(Iagente)
class ListaPersonal:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else: 
            self.__indice +=1
            nodoActual = self.__actual
            self.__actual = self.__actual.getSiguiente()
            return nodoActual
    
    def toJSON(self):
        d = []
        for i,nodo in enumerate(self):
            agente = nodo.getDato()
            d.append(agente.toJSON()) 
        return d
        
    def getTope(self):
        return self.__tope
        
    def ingresarDatos(self, tipo):
        datos = []
        print("Ingreso de datos")
        datos.append(input("Cuil: "))
        datos.append(input("Apellido: "))
        datos.append(input("Nombre: "))
        datos.append(float(input("Sueldo basico: ")))
        datos.append(int(input("Antiguedad: ")))
        match tipo:
            case "Docente":
                datos.append(input("Carrera que dicta: "))
                datos.append(input("Cargo: "))
                datos.append(input("Catedra: "))
                agente = Docente(*datos)
            case "Investigador":
                datos.append(input("Area de investigacion: "))
                datos.append(input("Tipo de investigacion: "))
                agente = Investigador(*datos)
            case "Docente Investigador":
                datos.append(input("Categoria en el programa de incentivos de investigacion: "))
                datos.append(float(input("Importe extra por docencia e investigacion: ")))
                agente = Investigador(*datos)
            case "Personal de Apoyo":
                datos.append(input("Categoria: "))
                agente = PersonalApoyo(*datos)
        return agente       

    def agregarElemento(self, agente):
        nodo = Nodo(agente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        if self.__tope == None:
            self.__tope = 0
        self.__tope +=1

    def insertarElemento(self, posicion, agente):
        if posicion <= self.__tope:
            nodoAguardar = Nodo(agente)
            backUpTope = self.__tope
            self.__tope = posicion-1
            for nodo in self:
                if self.__indice == self.__tope :
                    nodoAguardar.setSiguiente(nodo.getSiguiente())
                    nodo.setSiguiente(nodoAguardar)
            self.__tope = backUpTope +1
        else: print("IMPOSIBLE INGRESAR EN UN AUTO")

    def mostrarDatos(self):
        for nodo in self:
            print(nodo.getDato())

    def mostrarElemento(self,posicion):
        bandera = False
        while self.__indice < self.__tope and not bandera:
            nodo = self.__next__()
            if self.__indice == posicion:
                print(nodo.getDato())
                print(type(nodo.getDato()))
                bandera = True

    def nuevaLista(self, carreraAbuscar):
        nuevaLista = []
        for nodo in self:
            agente = nodo.getDato()
            if isinstance(agente, DocenteInvestigador):
                if carreraAbuscar == agente.getCarrera():
                    nuevaLista.append(agente)
        nuevaLista = sorted(nuevaLista, key=lambda docente: docente.getNombre())
        for docente in nuevaLista:
            print(docente)

    def contarDocentesYtrabajadores(self, areaDeInvestigacion):
        cantDocentesInvestigadores = self.contarDocentesInvestigadores()
        cantTInvestigadoresDeArea = self.contarInvestigadoresEnArea(areaDeInvestigacion)
        print(f"Hay {cantDocentesInvestigadores} Docentes Investigadores")
        print(f"Hay {cantTInvestigadoresDeArea} Investigadores que trabajan en {areaDeInvestigacion}")


    def contarDocentesInvestigadores(self):
        contador = 0
        for nodo in self:
            agente = nodo.getDato()
            if isinstance(agente, DocenteInvestigador):
                contador +=1
        return contador

    def contarInvestigadoresEnArea(self, areaInvestigacion):
        contador = 0
        for nodo in self:
            agente = nodo.getDato()
            if type(agente) == Investigador and agente.getAreaInvestigacion() == areaInvestigacion:
                contador +=1
        return contador
    #en este punto, cuidado con usar isinstance porque confunde investigadores
    #con DocenteInvestigadores ya que estos ultimos tambien son instancia de investigadores


    def generarListaOrdenadaYmostrar(self):
        listaOrdenada = []
        for nodo in self:
            agente = nodo.getDato()
            listaOrdenada.append(agente)
        listaOrdenada = sorted(listaOrdenada, key=lambda agente: agente.getApellido())
        for agente in listaOrdenada:
            print(type(agente))
            print(f"Apellido: {agente.getApellido()} Nombre: {agente.getNombre()}  Sueldo: {agente.getSueldo()}\n")

        
    
    def calculoImporteYmostrarDatos(self, categoria):
        sumaTotal = 0
        for nodo in self:
            agente = nodo.getDato()
            if type(agente) == DocenteInvestigador:
                if agente.getCategoria() == categoria:
                    print(f"{agente.getApellido()} {agente.getNombre()} {agente.getImporteExtra()}")
                    sumaTotal += sumaTotal + agente.getImporteExtra()
        print(f"El importe total de esa categoria es de {sumaTotal}")


    

    
    #Metodos de Interface Director--------------------------------------
    def modificarBasico(self, dni, nuevoBasico):
        print("Aca solo puede acceder el director, modificar basico")
    
    def modificarPorcentajePorCargo(self):
        print("Modificacion de porcentaje por cargo")
        cargo = input("Ingrese el cargo que desea modificar(Simple, Semiexclusivo, Exclusivo): ")
        porcentaje = int(input("Ingrese el nuevo porcentaje: "))/100
        Docente.modificarPorcentajeCargo(cargo, porcentaje)

    def modificarPorcentajePorCategoria(self, DNI, nuevoPorcentajeCategoria):
        print("Aca solo puede acceder el director, modificar porcentaje por categoria")

    def modificarImporteExtra(self, DNI, nuevoPorcentajeExtra):
        print("Aca solo puede acceder el director, modificar importe extra")

    #Metodo de Interface Tesorero--------------------------------------
    def gastosSueldoPorEmpleado(self, dni):
        bandera = False
        while self.__indice < self.__tope and not bandera:
            nodo = self.__next__()
            agente = nodo.getDato()
            if agente.getCuil().split("-")[1] == dni:
                print(f"Sueldo del agente: {agente.getSueldo()}")
                bandera = True