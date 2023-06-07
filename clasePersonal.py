

class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldoBasico: float
    __antiguedad: int

    def __init__(self, cuil=None, apellido=None, nombre=None, sueldoBasico=None, antiguedad=None) -> None:
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        if sueldoBasico == None:
            self.__sueldoBasico = sueldoBasico
        else: self.__sueldoBasico = float(sueldoBasico)
        if antiguedad == None:
            self.__sueldoBasico = antiguedad
        else: self.__antiguedad = int(antiguedad)

    def __str__(self) -> str:
        return f"{self.__cuil} {self.__apellido} {self.__nombre} {self.__sueldoBasico} {self.__antiguedad}"
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCuil(self):
        return self.__cuil
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            cuil=self.__cuil,  
                            apellido =self.__apellido,
                            nombre =self.__nombre,
                            sueldoBasico =self.__sueldoBasico,
                            antiguedad=self.__antiguedad,
            )
        )
        return d
    