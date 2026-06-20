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
        self.estado = "CUENTA_ACTIVA"

    def cargar_recursos(self, recurso: str):
        if len(self.__recursos_cuenta) >= 4:
            raise ValueError("Limite de recurso por atención alcanzado")
        return self.__recursos_cuenta.append(recurso)
    
    @property
    def acceder_lista_recursos(self):
        return tuple(self.__recursos_cuenta)
    
    def ciclo_calcular_multas(self):
        if self.estado == "CUENTA SUSPENDIDA":
            return
        
        if len(self.__recursos_cuenta) == 0:
            return 
        
        for recurso in self.__recursos_cuenta:
            recurso.calcular_penalizacion(recurso)
            
        suma_multa = sum(m.calcular_penalizacion() for m in self.__recursos_cuenta)
        promedio = suma_multa / len(self.__recursos_cuenta)
        
        if promedio > 15 or (self.bibliotecario.Bibliotecario.codigo_usuario ):
            return self.estado("CUENTA SUSPENDIDA")
     
     
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
        return self.horas_exceso * 2.25


class UsoSalaEstudio(Recurso):
    def __init__(self, codigo_identificador):
        super().__init__(codigo_identificador)
        self.alumnos_espera = []
    
    def calcular_penalizacion(self, factor_penalizacion: int):
        return self.horas_exceso * factor_penalizacion
        


