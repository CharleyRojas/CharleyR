def buscar_en_matriz():
    # Crear matriz 3x3
    matriz = [
        [5, 2, 9],
        [1, 8, 4],
        [7, 3, 6]
    ]

    # Mostrar matriz original
    print("Matriz 3x3:")
    for fila in matriz:
        print(fila)

    # Valor a buscar
    valor_buscar = 8

    # Buscar el valor en la matriz
    encontrado = False
    posicion = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscar:
                encontrado = True
                posicion = (i, j)
                break
        if encontrado:
            break

    # Mostrar resultado
    print(f"\nBuscando el valor: {valor_buscar}")
    if encontrado:
        print(f"Valor encontrado en la posición: Fila {posicion[0] + 1}, Columna {posicion[1] + 1}")
    else:
        print("Valor no encontrado en la matriz")


# Ejecutar el programa
if __name__ == "__main__":
    buscar_en_matriz()