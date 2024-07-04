def registrar_estudiante():
    # Solicitar nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")

    # Solicitar edad del estudiante
    edad = int(input("Ingrese la edad del estudiante: "))

    # Solicitar sexo del estudiante
    sexo = input("Ingrese el sexo del estudiante (M/F): ")
    while sexo.upper() not in ["M", "F"]:
        sexo = input("Ingrese el sexo del estudiante (M/F): ")

    # Solicitar promedio académico del estudiante
    promedio = float(input("Ingrese el promedio académico del estudiante: "))

    # Solicitar estado de activación del estudiante
    activo = input("¿El estudiante está activo? (S/N): ")
    while activo.upper() not in ["S", "N"]:
        activo = input("¿El estudiante está activo? (S/N): ")

    # Mostrar resumen de la información ingresada
    print("\nResumen del estudiante:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Sexo: {sexo.upper()}")
    print(f"Promedio académico: {promedio:.2f}")
    print(f"Estado de activación: {'Activo' if activo.upper() == 'S' else 'Inactivo'}")

registrar_estudiante()