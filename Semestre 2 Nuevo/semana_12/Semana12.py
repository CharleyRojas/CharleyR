import json
import os


class Libro:
    def __init__(self, titulo, autor, categoria):
        # Uso de TUPLA para atributos inmutables
        self.info = (titulo, autor)
        self.categoria = categoria

    @property
    def titulo(self): return self.info[0]

    @property
    def autor(self): return self.info[1]

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "categoria": self.categoria}

    def __str__(self):
        return f"📖 '{self.titulo}' | Autor: {self.autor} | Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario, libros_prestados=None):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # LISTA para gestionar libros prestados
        self.libros_prestados = libros_prestados if libros_prestados else []

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [l.to_dict() for l in self.libros_prestados]
        }

    def __str__(self):
        return f"👤 {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        # DICCIONARIO para libros (Título como clave) y CONJUNTO para IDs únicos
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()
        self.archivo_datos = "biblioteca_simple.json"
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "libros": [l.to_dict() for l in self.libros_disponibles.values()],
            "usuarios": [u.to_dict() for u in self.usuarios_registrados.values()]
        }
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("\n💾 Datos guardados en el archivo.")

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    for l in datos['libros']:
                        nuevo_libro = Libro(l['titulo'], l['autor'], l['categoria'])
                        self.libros_disponibles[l['titulo']] = nuevo_libro
                    for u in datos['usuarios']:
                        prestados = [Libro(lp['titulo'], lp['autor'], lp['categoria']) for lp in u['libros_prestados']]
                        nuevo_usuario = Usuario(u['nombre'], u['id_usuario'], prestados)
                        self.usuarios_registrados[u['id_usuario']] = nuevo_usuario
                        self.ids_usuarios.add(u['id_usuario'])
                print("📂 Datos cargados correctamente.")
            except:
                print("⚠️ No se pudo cargar el archivo, iniciando biblioteca vacía.")

    def anadir_libro(self, t, a, c):
        if t not in self.libros_disponibles:
            self.libros_disponibles[t] = Libro(t, a, c)
            print(f"✅ Libro '{t}' añadido al catálogo.")
        else:
            print(f"⚠️ El libro '{t}' ya existe en la biblioteca.")

    def registrar_usuario(self, n, id_u):
        if id_u not in self.ids_usuarios:
            self.ids_usuarios.add(id_u)
            self.usuarios_registrados[id_u] = Usuario(n, id_u)
            print(f"✅ Usuario '{n}' registrado.")
        else:
            print("⚠️ Este ID de usuario ya está en uso.")

    def prestar_libro(self, id_u, titulo):
        if id_u in self.ids_usuarios and titulo in self.libros_disponibles:
            libro = self.libros_disponibles.pop(titulo)
            self.usuarios_registrados[id_u].libros_prestados.append(libro)
            print(f"✅ '{titulo}' prestado a {self.usuarios_registrados[id_u].nombre}.")
        else:
            print("⚠️ Usuario no encontrado o el libro no está disponible.")

    def devolver_libro(self, id_u, titulo):
        if id_u in self.ids_usuarios:
            user = self.usuarios_registrados[id_u]
            for i, libro in enumerate(user.libros_prestados):
                if libro.titulo == titulo:
                    self.libros_disponibles[titulo] = user.libros_prestados.pop(i)
                    print(f"✅ '{titulo}' devuelto a la biblioteca.")
                    return
            print(f"⚠️ El usuario no tiene el libro '{titulo}'.")
        else:
            print("⚠️ ID de usuario no válido.")

    def listar_todo_el_catalogo(self):
        print("\n--- 📚 LIBROS DISPONIBLES EN ESTANTE ---")
        if not self.libros_disponibles:
            print("   (La biblioteca está vacía)")
        else:
            for libro in self.libros_disponibles.values():
                print(f"   {libro}")

    def listar_prestamos_usuario(self, id_u):
        if id_u in self.usuarios_registrados:
            user = self.usuarios_registrados[id_u]
            print(f"\n📚 Libros en posesión de {user.nombre}:")
            if not user.libros_prestados:
                print("   No tiene libros pendientes.")
            else:
                for l in user.libros_prestados: print(f"   - {l}")
        else:
            print("⚠️ Usuario no encontrado.")


# --- MENÚ DE NAVEGACIÓN ---
def menu():
    bib = Biblioteca()
    while True:
        print("\n" + "=" * 35 + "\n   SISTEMA DE GESTIÓN BIBLIOTECARIA\n" + "=" * 35)
        print("1. Ver Catálogo Disponible")
        print("2. Añadir Nuevo Libro")
        print("3. Registrar Usuario")
        print("4. Prestar Libro")
        print("5. Devolver Libro")
        print("6. Ver Libros de un Usuario")
        print("7. Salir y Guardar Todo")

        op = input("\nSeleccione una opción: ")

        if op == "1":
            bib.listar_todo_el_catalogo()
        elif op == "2":
            bib.anadir_libro(input("Título: "), input("Autor: "), input("Categoría: "))
        elif op == "3":
            bib.registrar_usuario(input("Nombre: "), input("ID: "))
        elif op == "4":
            bib.prestar_libro(input("ID Usuario: "), input("Título del Libro: "))
        elif op == "5":
            bib.devolver_libro(input("ID Usuario: "), input("Título del Libro: "))
        elif op == "6":
            bib.listar_prestamos_usuario(input("Ingrese ID del usuario: "))
        elif op == "7":
            bib.guardar_datos()
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("⚠️ Opción no válida.")


if __name__ == "__main__":
    menu()