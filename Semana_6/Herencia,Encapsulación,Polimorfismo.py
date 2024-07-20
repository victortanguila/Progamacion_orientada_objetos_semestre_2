# Definición de Objeto de Herencia, Encapsulación y Polimorfismo
# Clase Base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Atributos encapsulados
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__kilometraje = 0

    def descripcion(self):
        return f"Vehículo {self.__marca} {self.__modelo} del año {self.__año}"

    def avanzar(self, km):
        self.__kilometraje += km
        print(f"Avanzando {km} km. Kilometraje actual: {self.__kilometraje} km")

    def get_kilometraje(self):
        return self.__kilometraje


# Clase Derivada: Coche (hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def descripcion(self):
        # Polimorfismo: método sobrescrito
        return f"Coche {self._Vehiculo__marca} {self._Vehiculo__modelo} del año {self._Vehiculo__año} con {self.__puertas} puertas"

    def abrir_puertas(self):
        print("Abriendo puertas...")


# Clase Derivada: Moto (hereda de Vehiculo)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def descripcion(self):
        # Polimorfismo: método sobrescrito
        return f"Moto {self._Vehiculo__marca} {self._Vehiculo__modelo} del año {self._Vehiculo__año} con {self.__cilindrada} cc"

    def acelerar(self):
        print("Acelerando...")


# Crear instancias de las clases
vehiculo = Vehiculo("Toyota", "Corolla", 2015)
coche = Coche("Ford", "Focus", 2018, 5)
moto = Moto("Honda", "CBR", 2020, 600)

# Demostrar la funcionalidad de las clases
print("Vehículo:")
print(vehiculo.descripcion())
vehiculo.avanzar(100)
print(f"Kilometraje: {vehiculo.get_kilometraje()} km")
print()

print("Coche:")
print(coche.descripcion())
coche.avanzar(50)
print(f"Kilometraje: {coche.get_kilometraje()} km")
coche.abrir_puertas()
print()

print("Moto:")
print(moto.descripcion())
moto.avanzar(20)
print(f"Kilometraje: {moto.get_kilometraje()} km")
moto.acelerar()