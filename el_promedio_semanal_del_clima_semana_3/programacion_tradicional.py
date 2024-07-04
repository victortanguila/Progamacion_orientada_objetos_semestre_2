import random

# Definir las ciudades, días de la semana y semanas
ciudades = ['Quito', 'latacunga', 'Ambato']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas_enero = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Almacenamiento de matriz de temperaturas
temperaturas_diarias = [[[random.randint(0, 35) for _ in dias_semana] for _ in semanas_enero] for _ in ciudades]

# Calculando el promedio de temperaturas por ciudades y semanas
for ciudad, temperaturas_ciudad in zip(ciudades, temperaturas_diarias):
    print(f"Promedio de temperaturas para {ciudad}:")

    for semana, temperaturas_semana in zip(semanas_enero, temperaturas_ciudad):
        promedio = sum(temperatura for temperatura in temperaturas_semana) / len(temperaturas_semana)
        print(f"{semana}: {promedio:.2f} grados Celsius")

    print()