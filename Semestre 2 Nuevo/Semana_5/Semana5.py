"""
Programa: Gestor de Productos Simple
Descripción: Este programa permite gestionar información básica de productos,
             calcular el precio con impuesto y mostrar un resumen.
"""

def calcular_precio_con_impuesto(precio_base, tasa_impuesto):
    """
    Calcula el precio final de un producto incluyendo impuesto.

    Args:
        precio_base (float): Precio sin impuesto.
        tasa_impuesto (float): Tasa de impuesto en porcentaje (ej. 16 para 16%).

    Returns:
        float: Precio con impuesto aplicado.
    """
    impuesto = precio_base * (tasa_impuesto / 100)
    precio_final = precio_base + impuesto
    return precio_final


def mostrar_resumen_producto(nombre_producto, precio_base, disponible):
    """
    Muestra un resumen de la información del producto.

    Args:
        nombre_producto (str): Nombre del producto.
        precio_base (float): Precio base del producto.
        disponible (bool): Disponibilidad del producto.
    """
    print("\nResumen del producto:")
    print(f"   Nombre: {nombre_producto}")
    print(f"   Precio base: ${precio_base:.2f}")
    print(f"   Disponible: {'Si' if disponible else 'No'}")


def main():
    # Tipos de datos utilizados:
    #   - str: nombre_producto
    #   - float: precio_base, tasa_impuesto
    #   - bool: producto_disponible
    #   - int: cantidad_productos

    # Identificadores descriptivos en snake_case:
    nombre_producto = "Laptop Gamer"
    precio_base = 1200.50
    tasa_impuesto = 16.0
    producto_disponible = True
    cantidad_productos = 3

    # Mostrar información base:
    mostrar_resumen_producto(nombre_producto, precio_base, producto_disponible)

    # Cálculo con impuesto:
    precio_final = calcular_precio_con_impuesto(precio_base, tasa_impuesto)
    print(f"   Precio con impuesto ({tasa_impuesto}%): ${precio_final:.2f}")

    # Cálculo total si se compran varias unidades:
    if producto_disponible:
        total_sin_impuesto = precio_base * cantidad_productos
        total_con_impuesto = calcular_precio_con_impuesto(total_sin_impuesto, tasa_impuesto)
        print(f"\nComprando {cantidad_productos} unidades:")
        print(f"   Total sin impuesto: ${total_sin_impuesto:.2f}")
        print(f"   Total con impuesto: ${total_con_impuesto:.2f}")
    else:
        print("\nProducto no disponible para compra.")


# Punto de entrada del programa:
if __name__ == "__main__":
    main()