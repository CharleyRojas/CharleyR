"""
Sistema de Gestión de Biblioteca - Modelo POO
Este programa modela un sistema de biblioteca con libros, usuarios y préstamos.
"""


class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
            return False

    def devolver(self):
        self.disponible = True
        print(f"Libro '{self.titulo}' devuelto.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} - {estado}"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado: '{libro.titulo}'")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto: '{libro.titulo}'")
        else:
            print(f"{self.nombre} no tiene prestado el libro '{libro.titulo}'")

    def mostrar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"  - {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene libros prestados.")

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase que representa la biblioteca completa.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Libro agregado al catalogo: {libro.titulo}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre}")

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        print(f"Libro '{titulo}' no encontrado.")
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        print(f"Usuario con ID '{id_usuario}' no encontrado.")
        return None

    def mostrar_catalogo(self):
        print(f"Catalogo de la Biblioteca '{self.nombre}':")
        if self.catalogo:
            for libro in self.catalogo:
                print(f"  - {libro}")
        else:
            print("  (El catalogo esta vacio)")

    def mostrar_usuarios(self):
        print(f"Usuarios registrados en '{self.nombre}':")
        if self.usuarios:
            for usuario in self.usuarios:
                print(f"  - {usuario}")
        else:
            print("  (No hay usuarios registrados)")

    def __str__(self):
        return f"Biblioteca: {self.nombre} - Libros: {len(self.catalogo)} - Usuarios: {len(self.usuarios)}"


# Demostración del sistema
if __name__ == "__main__":
    print("=" * 60)
    print("SISTEMA DE GESTION DE BIBLIOTECA - DEMOSTRACION POO")
    print("=" * 60)

    # 1. Crear la biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # 2. Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "978-3-16-148410-0")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-1-23-456789-7")
    libro3 = Libro("1984", "George Orwell", "978-0-45-152493-5")

    # 3. Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # 4. Crear usuarios
    usuario1 = Usuario("Ana Garcia", "U001")
    usuario2 = Usuario("Carlos Lopez", "U002")

    # 5. Registrar usuarios en la biblioteca
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    print("\n" + "=" * 60)
    print("INFORMACION INICIAL DE LA BIBLIOTECA")
    print("=" * 60)
    biblioteca.mostrar_catalogo()
    biblioteca.mostrar_usuarios()

    print("\n" + "=" * 60)
    print("SIMULACION DE PRESTAMOS")
    print("=" * 60)

    # 6. Usuario 1 toma prestado un libro
    print("\nOperacion 1:")
    libro_prestar = biblioteca.buscar_libro("Cien años de soledad")
    if libro_prestar:
        usuario1.tomar_prestado(libro_prestar)

    # 7. Usuario 2 intenta tomar el mismo libro (debe fallar)
    print("\nOperacion 2:")
    if libro_prestar:
        usuario2.tomar_prestado(libro_prestar)

    # 8. Usuario 2 toma otro libro
    print("\nOperacion 3:")
    libro_prestar2 = biblioteca.buscar_libro("1984")
    if libro_prestar2:
        usuario2.tomar_prestado(libro_prestar2)

    print("\n" + "=" * 60)
    print("ESTADO ACTUAL DE LOS USUARIOS")
    print("=" * 60)
    usuario1.mostrar_libros_prestados()
    usuario2.mostrar_libros_prestados()

    print("\n" + "=" * 60)
    print("DEVOLUCION DE LIBROS")
    print("=" * 60)

    # 9. Usuario 1 devuelve el libro
    print("\nOperacion 4:")
    usuario1.devolver_libro(libro_prestar)

    # 10. Usuario 2 ahora puede tomar el libro
    print("\nOperacion 5:")
    usuario2.tomar_prestado(libro_prestar)

    print("\n" + "=" * 60)
    print("ESTADO FINAL DE LA BIBLIOTECA")
    print("=" * 60)
    biblioteca.mostrar_catalogo()

    print("\n" + "=" * 60)
    print("RESUMEN DE LA DEMOSTRACION")
    print("=" * 60)
    print("Se demostraron los siguientes conceptos de POO:")
    print("  1. Clases y objetos (Libro, Usuario, Biblioteca)")
    print("  2. Atributos y metodos")
    print("  3. Encapsulacion (atributos privados con getters/setters implicitos)")
    print("  4. Relaciones entre objetos (Usuario tiene Libros, Biblioteca tiene ambos)")
    print("  5. Metodos especiales (__str__ para representacion)")
    print("  6. Interaccion entre objetos (prestamos, devoluciones)")