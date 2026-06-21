import tkinter as tk
from tkinter import messagebox, ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada para nuevas tareas
        self.task_entry = ttk.Entry(self.root, width=30)
        self.task_entry.pack(pady=20)
        # Evento: Permitir añadir tarea con la tecla Enter
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        self.task_entry.focus()

        # Botones de acción
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Añadir Tarea", command=self.add_task).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Marcar Completada", command=self.complete_task).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Mostrar tareas en un Treeview (más moderno que Listbox)
        self.tree = ttk.Treeview(self.root, columns=("Estado"), show='headings', selectmode="browse")
        self.tree.heading("Estado", text="Tarea")
        self.tree.column("Estado", anchor="w")
        self.tree.pack(pady=10, fill="both", expand=True, padx=20)

        # Evento Opcional: Doble clic para marcar como completada
        self.tree.bind('<Double-1>', lambda event: self.complete_task())

    # --- Lógica de la Aplicación ---

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task != "":
            # Se inserta la tarea con un estado inicial
            self.tree.insert("", "end", values=(task,))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def complete_task(self):
        """Cambia el estado visual de la tarea para reflejar que está completada."""
        selected_item = self.tree.selection()
        if selected_item:
            current_values = self.tree.item(selected_item, 'values')
            # Si ya tiene el check, no hacemos nada o lo quitamos
            if "✔ " in current_values[0]:
                return

                # Modificamos el texto para mostrar que está completada
            new_value = f"✔ {current_values[0]}"
            self.tree.item(selected_item, values=(new_value,))
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para marcar.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()