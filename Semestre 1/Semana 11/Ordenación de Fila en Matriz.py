def ordenar_fila_matriz():
    # Crear matriz 3x3
    matriz = [
        [5, 2, 9],
        [1, 8, 4],
        [7, 3, 6]
    ]

    # Mostrar matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Elegir fila a ordenar (0-indexed)
    fila_a_ordenar = 1  # Segunda fila (índice 1)

    # Hacer una copia de la matriz para no modificar la original
    matriz_ordenada = [fila[:] for fila in matriz]

    # Ordenar la fila específica usando Bubble Sort (sencillo)
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # Ordenar la fila seleccionada
    matriz_ordenada[fila_a_ordenar] = bubble_sort(matriz_ordenada[fila_a_ordenar][:])

    # Mostrar resultado
    print(f"\nMatriz con la fila {fila_a_ordenar + 1} ordenada:")
    for fila in matriz_ordenada:
        print(fila)


# Ejecutar el programa
if __name__ == "__main__":
    ordenar_fila_matriz()