# un sistema de gestion de inventarios
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            return True
        return False

    def eliminar_producto(self, id):
        producto = self.buscar_producto_por_id(id)
        if producto is not None:
            self.productos.remove(producto)
            return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id)
        if producto is not None:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            return True
        return False

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        productos = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                productos.append(producto)
        return productos

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")


def main():
    inventario = Inventario()

    # Agregamos un producto
    producto = Producto(1, "Laptop", 5, 1000.00)
    inventario.agregar_producto(producto)

    while True:
        print("Menú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("Producto agregado con éxito")
            else:
                print("Error al agregar producto")
        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            if inventario.eliminar_producto(id):
                print("Producto eliminado con éxito")
            else:
                print("Error al eliminar producto")
        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            if inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado con éxito")
            else:
                print("Error al actualizar producto")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_productos_por_nombre(nombre)
            if productos:
                for producto in productos:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()