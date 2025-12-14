# ================================
# Programación Tradicional
# Promedio semanal del clima
# ================================

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de 7 días
    y las almacena en una lista.
    """
    temperaturas = []

    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal del programa.
    """
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
