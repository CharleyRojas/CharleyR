class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificamos si el ID ya existe antes de añadir
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
            return False
        self.productos.append(producto)
        print("Producto agregado con éxito.")
        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(f"Producto {id_producto} eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None: p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None: p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)