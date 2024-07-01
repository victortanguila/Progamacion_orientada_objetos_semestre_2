# Importar PyChart para graficar
import pychart

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Función para graficar el área
def graficar_area(area):
    data = [(1, area)]  # Datos para graficar (eje x, eje y)
    chart_object = pychart.PieChart2D()
    chart_object.add_dataset(data)
    chart_object.render()

# Ejemplo de uso
def main():
    # Variables con nombres en snake_case
    base_rectangulo = 5
    altura_rectangulo = 3
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

    # Imprimir el área calculada
    print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_rectangulo}")

    # Graficar el área
    graficar_area(area_rectangulo)

if _name_ == "_main_":
    main()