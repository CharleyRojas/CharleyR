# ============================================
#     Clase base: Persona
# ============================================

class Persona:
    def __init__(self, nombre, apellido, genero, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._genero = genero
        self._edad = edad

    def mostrar_info(self):
        return f"{self._nombre} {self._apellido} ({self._genero}), {self._edad} años"

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 1:
            self._nombre = nuevo_nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad


class Estudiante(Persona):
    def __init__(self, nombre, apellido, genero, edad, carrera):
        super().__init__(nombre, apellido, genero, edad)
        self.carrera = carrera

    def mostrar_info(self):
        return (f"Estudiante: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Carrera: {self.carrera}")


class Docente(Persona):
    def __init__(self, nombre, apellido, genero, edad, especialidad):
        super().__init__(nombre, apellido, genero, edad)
        self.especialidad = especialidad

    def mostrar_info(self):
        return (f"Docente: {self._nombre} {self._apellido} ({self._genero}), "
                f"{self._edad} años - Especialidad: {self.especialidad}")


# ============================================
#     PROGRAMA PRINCIPAL (uso de las clases)
# ============================================

p1 = Persona("Luis", "González", "M", 30)

# ← SOLO CAMBIADO: ahora e1 es tu ejemplo
e1 = Estudiante("charley", "rojas", "M", 20, "Ingeniería")

d1 = Docente("Ana", "Ramírez", "F", 40, "Programación")

print(p1.mostrar_info())
print(e1.mostrar_info())
print(d1.mostrar_info())

p1.set_nombre("Luis Alberto")
p1.set_edad(31)
print(p1.mostrar_info())
