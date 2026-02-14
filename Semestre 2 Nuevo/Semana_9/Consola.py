from producto import Producto
from inventario import Inventario


def menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            mi_inventario.agregar_producto(Producto(id_p, nom, cant, prec))

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cant = input("Nueva cantidad (deje en blanco para no cambiar): ")
            prec = input("Nuevo precio (deje en blanco para no cambiar): ")

            # Conversión segura de tipos
            cant = int(cant) if cant else None
            prec = float(prec) if prec else None
            mi_inventario.actualizar_producto(id_p, cant, prec)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nom)
            for r in resultados: print(r)

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    menu()