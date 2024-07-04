class SemanaClima:
    def __init__(self):
        """
        Constructor de la clase SemanaClima.
        Inicializa la lista vacía dias_clima donde se almacenarán los datos diarios del clima.
        """
        self.dias_clima = []

    def agregar_dia_clima(self, temperatura_maxima, temperatura_minima, precipitacion):
        """
        Método para agregar los datos del clima de un día.

        Args:
        - temperatura_maxima: Temperatura máxima del día.
        - temperatura_minima: Temperatura mínima del día.
        - precipitacion: Cantidad de precipitación en milímetros.

        Agrega un diccionario con los datos del clima del día a la lista dias_clima.
        Lanza una excepción si ya se han agregado 7 días de clima.
        """
        if len(self.dias_clima) < 7:
            self.dias_clima.append({
                'temperatura_maxima': temperatura_maxima,
                'temperatura_minima': temperatura_minima,
                'precipitacion': precipitacion
            })
        else:
            raise Exception("Ya se han agregado 7 días de clima")

    def calcular_promedio_temperatura_maxima(self):
        """
        Método para calcular el promedio de las temperaturas máximas de la semana.

        Returns:
        - Promedio de las temperaturas máximas de la semana, o 0 si no hay datos.
        """
        total = sum(dia['temperatura_maxima'] for dia in self.dias_clima)
        return total / len(self.dias_clima) if self.dias_clima else 0

    def calcular_promedio_temperatura_minima(self):
        """
        Método para calcular el promedio de las temperaturas mínimas de la semana.

        Returns:
        - Promedio de las temperaturas mínimas de la semana, o 0 si no hay datos.
        """
        total = sum(dia['temperatura_minima'] for dia in self.dias_clima)
        return total / len(self.dias_clima) if self.dias_clima else 0

    def calcular_promedio_precipitacion(self):
        """
        Método para calcular el promedio de la precipitación de la semana.

        Returns:
        - Promedio de la precipitación de la semana, o 0 si no hay datos.
        """
        total = sum(dia['precipitacion'] for dia in self.dias_clima)
        return total / len(self.dias_clima) if self.dias_clima else 0

    def mostrar_informacion_semanal(self):
        """
        Método para mostrar la información semanal del clima.

        Imprime los detalles de cada día (temperaturas máxima y mínima, precipitación)
        y los promedios de temperatura máxima, temperatura mínima y precipitación de la semana.
        """
        if not self.dias_clima:
            print("No hay información de clima disponible.")
            return

        for i, dia in enumerate(self.dias_clima):
            print(f"Día {i + 1}:")
            print(f"  Temperatura Máxima: {dia['temperatura_maxima']}°C")
            print(f"  Temperatura Mínima: {dia['temperatura_minima']}°C")
            print(f"  Precipitación: {dia['precipitacion']} mm")

        print(f"Promedio Temperatura Máxima: {self.calcular_promedio_temperatura_maxima()}°C")
        print(f"Promedio Temperatura Mínima: {self.calcular_promedio_temperatura_minima()}°C")
        print(f"Promedio Precipitación: {self.calcular_promedio_precipitacion()} mm")


# Semana Clima
semana_clima = SemanaClima()
semana_clima.agregar_dia_clima(30, 20, 5)  # Día 1
semana_clima.agregar_dia_clima(32, 21, 0)  # Día 2
semana_clima.agregar_dia_clima(28, 19, 10)  # Día 3
semana_clima.agregar_dia_clima(27, 18, 3)  # Día 4
semana_clima.agregar_dia_clima(31, 22, 1)  # Día 5
semana_clima.agregar_dia_clima(29, 20, 2)  # Día 6
semana_clima.agregar_dia_clima(33, 23, 0)  # Día 7

semana_clima.mostrar_informacion_semanal()