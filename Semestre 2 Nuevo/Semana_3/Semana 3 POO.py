# ================================
# Programación Orientada a Objetos
# Promedio semanal del clima
# ================================

class ClimaSemanal:
    """
    Clase que representa la información climática semanal.
    """

    def __init__(self):
        # Encapsulamiento de los datos
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas de los 7 días.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal.
        """
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("=== Promedio Semanal del Clima (POO) ===")

    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
