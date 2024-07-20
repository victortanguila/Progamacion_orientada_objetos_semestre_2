import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana_2 1/ Tecnicas_de_Programacion/tecnicas_de_programacion.py',
        '2': 'Semana_3 1/ Clima/clima.py/Tadicional/tradicional.py',
        '3': 'Semana_4 1/ Mundo_Real/mundo_real.py',
        '4': 'Semana_5 1/ Tipos_de_datos/tipos_de_datos.py',
        '5': 'Semana_6 1/ Herencia_Encapsulacion_Polimorfismo/herencia_encapsulacion_polimorfismo.py',
        '6': 'Semana_7 1/ Constructores_Destructores/constructores_destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard********")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()