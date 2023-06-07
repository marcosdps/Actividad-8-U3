from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoriaProgramaIncentivos: str  #categoria en el programa de incentivos de investigacion
    __importeExtra: float   #importe extra por docencia e investigacion
    
    def __init__(self, cuil=None, apellido=None, nombre=None, sueldoBasico=None, antiguedad=None, carreraDicta=None, cargo=None, catedra=None, areaInvestigacion=None, tipoDeInvestigacion=None, categoriaProgramaIncentivos=None, importeExtra=None):
        Docente.__init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carreraDicta, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, areaInvestigacion, tipoDeInvestigacion)
        self.__categoriaProgramaIncentivos = categoriaProgramaIncentivos
        self.__importeExtra = importeExtra 

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__categoriaProgramaIncentivos} {self.__importeExtra}"
    
    def getCarrera(self):
        return self._Docente__carreraDicta
        #Otra forma: return Docente.getCarreraDicta(self)
    
    
    def getNombre(self):
        return self._Personal__nombre
        #Otra forma: return Personal.getNombre(self)

    def getSueldo(self):
        return (super().getSueldo()+self.__importeExtra)
    
    def getCategoria(self):
        return self.__categoriaProgramaIncentivos
    
    def getImporteExtra(self):
        return self.__importeExtra
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            cuil=self._Personal__cuil,  
                            apellido =self._Personal__apellido,
                            nombre =self._Personal__nombre,
                            sueldoBasico =self._Personal__sueldoBasico,
                            antiguedad=self._Personal__antiguedad,
                            carreraDicta=self._Docente__carreraDicta,
                            cargo=self._Docente__cargo,
                            catedra=self._Docente__catedra,
                            areaInvestigacion=self._Investigador__areaInvestigacion,
                            tipoDeInvestigacion=self._Investigador__tipoDeInvestigacion,
                            categoriaProgramaIncentivos=self.__categoriaProgramaIncentivos,
                            importeExtra=self.__importeExtra               
            )
        )
        return d