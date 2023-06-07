from claseDocente import Docente
from clasePersonal import Personal
from claseApoyo import PersonalApoyo
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from pathlib import Path
import json

class ObjectEncoder:
    def leerArchivoJSON(self, archivo):
        with Path(archivo).open(encoding="UTF-8")as archi:
            diccionario=json.load(archi)
        return diccionario
    
    def decodificador(self, diccionario, lista):
        for datos in diccionario:
            clase = datos["__class__"]
            atributos = datos["__atributos__"]
            match(clase):
                case "Docente":
                    agente = Docente(**atributos)
                    lista.agregarElemento(agente)
                case "Investigador":
                    agente = Investigador(**atributos)
                    lista.agregarElemento(agente)
                case "DocenteInvestigador":
                    agente = DocenteInvestigador(**atributos)
                    lista.agregarElemento(agente)
                case "PersonalApoyo":
                    agente = PersonalApoyo(**atributos)
                    lista.agregarElemento(agente)
        return agente
    
    def guardarDatos(self, diccionario):
        with open("personal.json", "w", encoding="UTF-8")as archi:
            json.dump(diccionario, archi, indent=4)
            archi.close