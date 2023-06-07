from clasePersonal import Personal

class Investigador(Personal):
    __areaInvestigacion: str
    __tipoDeInvestigacion: str

    def __init__(self, cuil=None, apellido=None, nombre=None, sueldoBasico=None, antiguedad=None, areaInvestigacion=None, tipoDeInvestigacion=None) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoDeInvestigacion = tipoDeInvestigacion

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__areaInvestigacion} {self.__tipoDeInvestigacion}"
    

    def getAreaInvestigacion(self):
        return self.__areaInvestigacion
    
    def getSueldo(self):
        return (self._Personal__sueldoBasico + (self._Personal__sueldoBasico*(0.01*self._Personal__antiguedad)))
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            cuil=self._Personal__cuil,  
                            apellido =self._Personal__apellido,
                            nombre =self._Personal__nombre,
                            sueldoBasico =self._Personal__sueldoBasico,
                            antiguedad=self._Personal__antiguedad,
                            areaInvestigacion=self.__areaInvestigacion,
                            tipoDeInvestigacion=self.__tipoDeInvestigacion
            )
        )
        return d