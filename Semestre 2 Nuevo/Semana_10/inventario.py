from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo de texto al iniciar."""
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    # Formato esperado: id,nombre,cantidad,precio
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        p = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                        self.productos.append(p)
            print(f"Sistema: Inventario cargado exitosamente desde {self.archivo}.")
        except FileNotFoundError:
            # Si no existe, se crea el archivo vacío según el requisito 3
            print(f"Sistema: El archivo {self.archivo} no existe. Creando uno nuevo...")
            open(self.archivo, "w").close()
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo con la lista actual de productos."""
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            return True
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")
            return False

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe.")
            return False

        self.productos.append(producto)
        if self.guardar_en_archivo():
            print(f"Producto '{producto.get_nombre()}' añadido y guardado en archivo.")
            return True
        return False

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                nombre = p.get_nombre()
                self.productos.remove(p)
                if self.guardar_en_archivo():
                    print(f"Producto '{nombre}' eliminado del archivo.")
                    return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None: p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None: p.set_precio(nuevo_precio)
                if self.guardar_en_archivo():
                    print("Producto actualizado y cambios guardados.")
                    return True
        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)