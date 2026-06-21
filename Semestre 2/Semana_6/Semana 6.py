# Clase base: Empleado
# ...........................
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos públicos
        self.nombre = nombre

        # Atributo privado (Encapsulación)
        self.__salario = salario

    # Método para obtener el salario (getter)
    def get_salario(self):
        return self.__salario

    # Método para modificar el salario (setter)
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser mayor a 0")

    # Método que será sobrescrito (Polimorfismo)
    def calcular_salario(self):
        return self.__salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: {self.get_salario()}")


# Clase derivada: EmpleadoTiempoCompleto
# ............................
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        # Llamada al constructor de la clase base (Herencia)
        super().__init__(nombre, salario)
        self.bono = bono

    # Sobrescritura del método (Polimorfismo)
    def calcular_salario(self):
        return self.get_salario() + self.bono

    def mostrar_info(self):
        print(f"Empleado Tiempo Completo: {self.nombre}, "
              f"Salario Total: {self.calcular_salario()}")


# Programa principal
# ..........................
if __name__ == "__main__":
    # Crear objeto de la clase base
    empleado1 = Empleado("Carlos", 500)
    empleado1.mostrar_info()

    # Crear objeto de la clase derivada
    empleado2 = EmpleadoTiempoCompleto("Ana", 800, 200)
    empleado2.mostrar_info()

    # Demostración de encapsulación
    empleado1.set_salario(600)
    print(f"Nuevo salario de {empleado1.nombre}: {empleado1.get_salario()}")

    # Demostración de polimorfismo
    empleados = [empleado1, empleado2]
    print("\nCálculo de salarios usando polimorfismo:")
    for emp in empleados:
        print(f"{emp.nombre}: {emp.calcular_salario()}")
