from excepciones import ClienteInvalidoError


class Cliente:
    def __init__(self, nombre, identificacion, correo, telefono):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)
        self.set_telefono(telefono)

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío")
        self.__nombre = nombre
    def set_identificacion(self, identificacion):
        if not str(identificacion).isdigit():
            raise ClienteInvalidoError("La identificación debe contener números")
        self.__identificacion = identificacion

    def set_correo(self, correo):
        if "@" not in correo:
            raise ClienteInvalidoError("Correo inválido")
        self.__correo = correo

    def set_telefono(self, telefono):
        if not str(telefono).isdigit():
            raise ClienteInvalidoError("Teléfono inválido")
        self.__telefono = telefono
    
     def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"ID: {self.__identificacion} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

