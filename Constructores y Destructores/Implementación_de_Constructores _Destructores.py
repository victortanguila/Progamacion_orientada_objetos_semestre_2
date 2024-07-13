# Clase que representa una persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una persona llamada {self.nombre} con {self.edad} años.")

    def __del__(self):
        print(f"Se ha eliminado la persona llamada {self.nombre}.")

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class ConexionBaseDatos:
    def __init__(self, servidor, usuario, password):
        self.servidor = servidor
        self.usuario = usuario
        self.password = password
        self.conexion = self.establecer_conexion()

    def __del__(self):
        self.cerrar_conexion()

    def establecer_conexion(self):
        print("Conexión establecida")
        return True

    def cerrar_conexion(self):
        print("Conexión cerrada")

class Libro:
    def __init__(self, titulo, autor, anio_publicacion=2022):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        print(f"Se ha creado un libro llamado {self.titulo} de {self.autor} publicado en {self.anio_publicacion}.")

    def __del__(self):
        print(f"Se ha eliminado el libro llamado {self.titulo}.")

# Crear objetos
persona = Persona("Victor", 37)
conexion = ConexionBaseDatos("localhost", "root", "password")
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954)

# Utilizar objetos
persona.saludar()
print("Conectando a la base de datos...")
# ...

# Eliminar objetos
del persona
del conexion
del libro1
del libro2