from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        if duracion <= 0:
            raise ServicioNoDisponibleError(
                "Duración inválida"
            )

        costo = self.precio_base * duracion
        return costo - (costo * descuento)

    def descripcion(self):
        return "Servicio de reserva de salas"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        if duracion <= 0:
            raise ServicioNoDisponibleError(
                "Tiempo inválido"
            )

        costo = (
            self.precio_base * duracion
        ) + 20000

        return costo - (costo * descuento)

    def descripcion(self):
        return (
            "Servicio de alquiler de equipos"
        )


class AsesoriaEspecializada(Servicio):
    def calcular_costo(
        self,
        duracion,
        descuento=0
    ):
        if duracion <= 0:
            raise ServicioNoDisponibleError(
                "Duración incorrecta"
            )

        costo = (
            self.precio_base
            * duracion
            * 1.2
        )

        return costo - (costo * descuento)

    def descripcion(self):
        return (
            "Servicio de asesoría especializada"
        )

