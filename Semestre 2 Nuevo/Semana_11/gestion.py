import json
import os


class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self): return self.id

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    def set_cantidad(self, nueva_cantidad): self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio): self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Stock: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self, nombre_archivo="inventario_datos.txt"):
        self.nombre_archivo = nombre_archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto registrado exitosamente.")

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod]
            self.guardar_en_archivo()
            print(f"Producto {id_prod} eliminado.")
        else:
            print("Error: ID no encontrado.")

    def actualizar_producto(self, id_prod, cantidad=None, precio=None):
        if id_prod in self.productos:
            if cantidad is not None: self.productos[id_prod].set_cantidad(cantidad)
            if precio is not None: self.productos[id_prod].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Error: ID inexistente.")

    def buscar_por_nombre(self, nombre_buscar):
        encontrados = [p for p in self.productos.values() if nombre_buscar.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados: print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario esta vacio.")
        else:
            for p in self.productos.values(): print(p)

    def guardar_en_archivo(self):
        datos = [v.__dict__ for v in self.productos.values()]
        with open(self.nombre_archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_desde_archivo(self):
        if os.path.exists(self.nombre_archivo):
            try:
                with open(self.nombre_archivo, 'r') as f:
                    for d in json.load(f):
                        self.productos[d['id']] = Producto(d['id'], d['nombre'], d['cantidad'], d['precio'])
            except:
                pass


# --- Función de apoyo para lectura con cancelación ---
def leer_entrada(mensaje):
    entrada = input(f"{mensaje} (o escribe 'cancelar'): ").strip()
    if entrada.lower() == 'cancelar':
        return None
    return entrada


def ejecutar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- MENU DE GESTION (Escribe 'cancelar' para abortar operacion) ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Mostrar | 6. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            id_p = leer_entrada("ID")
            if id_p is None: continue

            nom = leer_entrada("Nombre")
            if nom is None: continue

            can_str = leer_entrada("Cantidad")
            if can_str is None: continue

            pre_str = leer_entrada("Precio")
            if pre_str is None: continue

            try:
                mi_inventario.añadir_producto(Producto(id_p, nom, int(can_str), float(pre_str)))
            except ValueError:
                print("Error: Datos numericos invalidos.")

        elif opcion == "2":
            id_b = leer_entrada("ID a eliminar")
            if id_b: mi_inventario.eliminar_producto(id_b)

        elif opcion == "3":
            id_e = leer_entrada("ID a actualizar")
            if id_e is None: continue

            can = leer_entrada("Nueva cantidad (vacio para omitir)")
            if can is None: continue

            pre = leer_entrada("Nuevo precio (vacio para omitir)")
            if pre is None: continue

            mi_inventario.actualizar_producto(id_e, int(can) if can else None, float(pre) if pre else None)

        elif opcion == "4":
            nom_b = leer_entrada("Nombre a buscar")
            if nom_b: mi_inventario.buscar_por_nombre(nom_b)

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            break


if __name__ == "__main__":
    ejecutar_menu()