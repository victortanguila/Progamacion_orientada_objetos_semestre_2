# biblioteca

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.año}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)


# Gestion de una biblioteca
biblioteca = Biblioteca("Biblioteca Nacional")

libro1 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("La Iliada", "Homero", 800)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print("Libros de la biblioteca:")
biblioteca.mostrar_libros()