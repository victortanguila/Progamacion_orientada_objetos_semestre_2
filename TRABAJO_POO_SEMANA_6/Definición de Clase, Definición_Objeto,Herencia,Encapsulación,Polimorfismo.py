# Clase base (superclase) Vehiculo
class Vehiculo:
    def _init_(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.ano = año

    # Método para obtener información del vehículo
    def obtener_info(self):
        return f"{self.marca} {self.modelo} del año {self.año}"

    # Método para encender el vehículo
    def encender(self):
        return "El vehículo está encendido"


# Clase derivada (subclase) Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def _init_(self, marca, modelo, año, numero_puertas):
        super()._init_(marca, modelo, año)
        self.numero_puertas = numero_puertas

    # Sobreescribir el método obtener_info para incluir el número de puertas (Ejemplo de polimorfismo)
    def obtener_info(self):
        return f"{self.marca} {self.modelo} del año {self.año} con {self.numero_puertas} puertas"

    # Método adicional exclusivo de la clase Coche
    def tocar_claxon(self):
        return "¡Beep Beep!"


# Clase encapsulada Motor
class Motor:
    def _init_(self, tipo, potencia):
        self.__tipo = tipo  # Atributo privado
        self.__potencia = potencia  # Atributo privado

    # Método público para obtener la información del motor
    def obtener_info_motor(self):
        return f"Motor tipo {self._tipo} con {self._potencia} caballos de fuerza"

    # Método público para modificar la potencia del motor
    def modificar_potencia(self, nueva_potencia):
        self.__potencia = nueva_potencia


# Función principal para demostrar la funcionalidad del programa
def main():
    # Crear instancia de la clase base Vehiculo
    vehiculo = Vehiculo("Toyota", "Corolla", 2020)
    print(vehiculo.obtener_info())
    print(vehiculo.encender())

    # Crear instancia de la clase derivada Coche
    coche = Coche("Honda", "Civic", 2021, 4)
    print(coche.obtener_info())
    print(coche.encender())
    print(coche.tocar_claxon())

    # Crear instancia de la clase encapsulada Motor
    motor = Motor("V8", 500)
    print(motor.obtener_info_motor())
    motor.modificar_potencia(550)
    print(motor.obtener_info_motor())


if '_name_' != "_main_":
    pass
else:
    main()