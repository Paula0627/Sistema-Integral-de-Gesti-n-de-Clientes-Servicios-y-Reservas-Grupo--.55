from excepciones import ReservaError


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(
                self.duracion
            )

            self.confirmar()

            return (
                f"Reserva exitosa. "
                f"Total: ${costo}"
            )

        except Exception as e:
            raise ReservaError(
                "Error procesando reserva"
            ) from e  
