from abc import ABC, abstractmethod

class Bibliotecario():
    def __init__(self, codigo_usuario, nombre_empleado):
        self.codigo_usuario = codigo_usuario 
        self.nombre_empleado = nombre_empleado
    
    
class RegistroAtencion():
    def __init__(self, codigo, carnet_alumno, codigo_usuario, nombre_empleado):
        self.codigo = codigo
        self.carnet_alumno = carnet_alumno
        self.__recursos_cuenta = []
        self.bibliotecario = Bibliotecario(codigo_usuario, nombre_empleado)

    def cargar_recursos(self, recurso: str):
        if len(self.__recursos_cuenta) > 4:
            raise ValueError("Limite de recurso por atención alcanzado")
        return self.__recursos_cuenta.append(recurso)
    
    @property
    def acceder_lista_recursos(self):
        return tuple(self.__recursos_cuenta)
    
    
class Recurso(ABC):
    def __init__(self, codigo_identificador):
        self.codigo_identificador = codigo_identificador
        self.horas_exceso = 0
        
    @abstractmethod
    def calcular_penalizacion(self, factor_penalizacion: int):
        pass
    

class PrestamoLibro(Recurso):
    def __init__(self, codigo_identificador):
        super().__init__(codigo_identificador)
        
    def calcular_penalizacion(self, factor_penalizacion: int):
        multa = self.horas_exceso * 2.25

class UsoSaalaEstudio(Recurso):
    def __init__(self, codigo_identificador):
        super().__init__(codigo_identificador)
        self.alumnos_espera = []
    
    def calcular_penalizacion(self, factor_penalizacion: int):
        multa = self.horas_exceso * factor_penalizacion