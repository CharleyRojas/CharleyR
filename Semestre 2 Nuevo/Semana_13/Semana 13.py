import tkinter as tk
from tkinter import messagebox


# --- Funcionalidad (Sección 2 y 3 de la tarea) ---

def agregar_dato():
    # Obtener el texto del campo de entrada
    informacion = entrada.get()

    # Validar que no esté vacío
    if informacion.strip():
        # Insertar en la lista (Listbox)
        lista_datos.insert(tk.END, informacion)
        # Limpiar el campo de texto para una nueva entrada
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")


def limpiar_todo():
    # Borrar el texto del campo de entrada
    entrada.delete(0, tk.END)
    # Borrar todos los elementos de la lista
    lista_datos.delete(0, tk.END)


# --- Diseño de la Interfaz (Sección 1 de la tarea) ---

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("300x450")

# 1. Etiquetas (labels)
lbl_instruccion = tk.Label(ventana, text="Ingrese información:", font=("Arial", 10, "bold"))
lbl_instruccion.pack(pady=10)

# 2. Campos de texto (entry)
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# 3. Botón "Agregar"
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, width=15)
btn_agregar.pack(pady=5)

# 4. Lista o tabla para mostrar datos (listbox)
lista_datos = tk.Listbox(ventana, width=35, height=12)
lista_datos.pack(pady=10, padx=10)  # <-- Corregido: 'padx' en lugar de 'px'

# 5. Botón "Limpiar"
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_todo, width=15)
btn_limpiar.pack(pady=5)

# Iniciar el ciclo de la aplicación
ventana.mainloop()