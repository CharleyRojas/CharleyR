import json
import os


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Uso de TUPLA para atributos inmutables (Requisito 1)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self): return self.info[0]

    @property
    def autor(self): return self.info[1]

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "categoria": self.categoria, "isbn": self.isbn}

    def __str__(self):
        return f"📖 '{self.titulo}' | Autor: {self.autor} | ISBN: {self.isbn} | Cat: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario, libros_prestados=None):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Uso de LISTA para gestionar libros (Requisito 3)
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
        # DICCIONARIO para libros (ISBN como clave) y CONJUNTO para IDs únicos (Requisito 1 & 3)
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()
        self.archivo_datos = "biblioteca_data.json"
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "libros": [l.to_dict() for l in self.libros_disponibles.values()],
            "usuarios": [u.to_dict() for u in self.usuarios_registrados.values()]
        }
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("\n💾 ¡Datos guardados en el archivo JSON!")

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                for l in datos['libros']:
                    nuevo_libro = Libro(l['titulo'], l['autor'], l['categoria'], l['isbn'])
                    self.libros_disponibles[l['isbn']] = nuevo_libro
                for u in datos['usuarios']:
                    prestados = [Libro(lp['titulo'], lp['autor'], lp['categoria'], lp['isbn']) for lp in
                                 u['libros_prestados']]
                    nuevo_usuario = Usuario(u['nombre'], u['id_usuario'], prestados)
                    self.usuarios_registrados[u['id_usuario']] = nuevo_usuario
                    self.ids_usuarios.add(u['id_usuario'])

    def anadir_libro(self, t, a, c, i):
        if i not in self.libros_disponibles:
            self.libros_disponibles[i] = Libro(t, a, c, i)
            print(f"✅ Libro '{t}' añadido.")
        else:
            print("⚠️ El ISBN ya existe.")

    def registrar_usuario(self, n, id_u):
        if id_u not in self.ids_usuarios:
            self.ids_usuarios.add(id_u)
            self.usuarios_registrados[id_u] = Usuario(n, id_u)
            print(f"✅ Usuario '{n}' registrado.")
        else:
            print("⚠️ Este ID ya está en uso.")

    def prestar_libro(self, id_u, isbn):
        if id_u in self.ids_usuarios and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_registrados[id_u].libros_prestados.append(libro)
            print(f"✅ Préstamo realizado a {self.usuarios_registrados[id_u].nombre}.")
        else:
            print("⚠️ Usuario no existe o libro no disponible.")

    def devolver_libro(self, id_u, isbn):
        if id_u in self.ids_usuarios:
            user = self.usuarios_registrados[id_u]
            for i, libro in enumerate(user.libros_prestados):
                if libro.isbn == isbn:
                    self.libros_disponibles[isbn] = user.libros_prestados.pop(i)
                    print("✅ Devolución exitosa.")
                    return
            print("⚠️ El usuario no tiene ese libro.")
        else:
            print("⚠️ Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        valor = valor.lower()
        encontrados = [l for l in self.libros_disponibles.values()
                       if valor in str(getattr(l, criterio)).lower()]
        if encontrados:
            for l in encontrados: print(f"  {l}")
        else:
            print("🔍 No se encontraron coincidencias.")

    def listar_prestamos_usuario(self, id_u):
        if id_u in self.usuarios_registrados:
            user = self.usuarios_registrados[id_u]
            print(f"\n📚 Libros de {user.nombre}:")
            if not user.libros_prestados:
                print("   Sin libros pendientes.")
            else:
                for l in user.libros_prestados: print(f"   - {l}")
        else:
            print("⚠️ Usuario no encontrado.")


# --- NAVEGACIÓN PRINCIPAL ---
def menu():
    bib = Biblioteca()
    while True:
        print("\n" + "=" * 30 + "\n  SISTEMA DE BIBLIOTECA\n" + "=" * 30)
        print("1. Añadir Libro\n2. Registrar Usuario\n3. Prestar Libro\n4. Devolver Libro")
        print("5. Buscar Libro\n6. Listar Libros de Usuario\n7. Salir y Guardar")

        op = input("\nSeleccione una opción: ")

        if op == "1":
            bib.anadir_libro(input("Título: "), input("Autor: "), input("Categoría: "), input("ISBN: "))
        elif op == "2":
            bib.registrar_usuario(input("Nombre: "), input("ID: "))
        elif op == "3":
            bib.prestar_libro(input("ID Usuario: "), input("ISBN Libro: "))
        elif op == "4":
            bib.devolver_libro(input("ID Usuario: "), input("ISBN Libro: "))
        elif op == "5":
            print("Buscar por: 1.Titulo | 2.Autor | 3.Categoria")
            c = {"1": "titulo", "2": "autor", "3": "categoria"}.get(input("Opción: "), "titulo")
            bib.buscar_libro(c, input("Texto a buscar: "))
        elif op == "6":
            bib.listar_prestamos_usuario(input("Ingrese ID del usuario: "))
        elif op == "7":
            bib.guardar_datos()
            print("¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    menu()