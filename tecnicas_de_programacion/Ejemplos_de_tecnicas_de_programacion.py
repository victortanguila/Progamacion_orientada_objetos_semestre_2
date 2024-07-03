# Abstracción: Definimos una clase abstracta Vehiculo
from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca  # Encapsulación: Uso de atributos privados
        self._modelo = modelo

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    def obtener_informacion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"


# Encapsulacion: La clase Coche hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas  # Encapsulación: Uso de atributos privados

    def arrancar(self):
        return "El coche ha arrancado"

    def detener(self):
        return "El coche se ha detenido"

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Puertas: {self._puertas}"


# Herencia: La clase Moto hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo  # Encapsulación: Uso de atributos privados

    def arrancar(self):
        return "La moto ha arrancado"

    def detener(self):
        return "La moto se ha detenido"

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Tipo: {self._tipo}"


# Polimorfismo: Usamos una lista de vehículos y llamamos a métodos que se comportan de manera diferente
vehiculos = [
    Coche("Toyota", "Corolla", 4),
    Moto("Harley Davidson", "Sportster", "Cruiser")
]

for vehiculo in vehiculos:
    print(vehiculo.arrancar())
    print(vehiculo.detener())
    print(vehiculo.obtener_informacion())
    print("-" * 30)
