from clasePersonal import Personal

class Docente(Personal):
    __carreraDicta: str
    __cargo: str
    __catedra: str
    __simple = 0.1
    __semiexclusivo = 0.2
    __exclusivo = 0.5

    def __init__(self, cuil=None, apellido=None, nombre=None, sueldoBasico=None, antiguedad=None, carreraDicta=None, cargo=None, catedra=None) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__carreraDicta = carreraDicta
        self.__cargo = cargo
        self.__catedra = catedra

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__carreraDicta} {self.__cargo} {self.__catedra}"
    
    def getCarreraDicta(self):
        return self.__carreraDicta
    
    def getSueldo(self):
        match(self.__cargo):
            case "Simple":
                porcentaje = self.__simple
            case "Semiexclusivo":
                porcentaje = self.__semiexclusivo
            case "Exclusivo":
                porcentaje = self.__exclusivo
        return (self._Personal__sueldoBasico + ((0.1* self._Personal__antiguedad)*self._Personal__sueldoBasico)  + self._Personal__sueldoBasico*porcentaje)
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            cuil=self._Personal__cuil,  
                            apellido =self._Personal__apellido,
                            nombre =self._Personal__nombre,
                            sueldoBasico =self._Personal__sueldoBasico,
                            antiguedad=self._Personal__antiguedad,
                            carreraDicta=self.__carreraDicta,
                            cargo=self.__cargo,
                            catedra=self.__catedra

            )
        )
        return d
    
    @classmethod
    def modificarPorcentajeCargo(cls, cargo, porcentaje):
        match(cargo):
            case "Simple":
                cls.__simple = porcentaje
            case "Semiexclusivo":
                cls.__semiexclusivo = porcentaje
            case "Exclusivo":
                cls.__exclusivo = porcentaje
                
