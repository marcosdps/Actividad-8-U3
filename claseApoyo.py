from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria: int

    def __init__(self, cuil=None, apellido=None, nombre=None, sueldoBasico=None, antiguedad=None, categoria=None) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = int(categoria)

    def __str__(self) -> str:
        return f"{super().__str__()} {self.__categoria}"
    
    def getSueldo(self):
        categoria = self.__categoria
        if 1 <= categoria <= 10:
            porcentaje = 0.1
        elif 11 <= categoria <= 20:
            porcentaje = 0.2
        elif 21 <= categoria <= 22:
            porcentaje = 0.3
        return (self._Personal__sueldoBasico + (self._Personal__sueldoBasico*(0.01*self._Personal__antiguedad))+ (self._Personal__sueldoBasico*porcentaje))
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                            cuil=self._Personal__cuil,  
                            apellido =self._Personal__apellido,
                            nombre =self._Personal__nombre,
                            sueldoBasico =self._Personal__sueldoBasico,
                            antiguedad=self._Personal__antiguedad,
                            categoria=self.__categoria
            )
        )
        return d