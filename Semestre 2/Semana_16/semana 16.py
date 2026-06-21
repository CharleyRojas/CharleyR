import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)
        self.task_entry.focus_set()  # Iniciar con el foco en el input

        # Botones de acción
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_button = tk.Button(btn_frame, text="Añadir (Enter)", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Completar (C)", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar (Del)", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # --- Atajos de Teclado (Bindings) ---

        # Vincular teclas a funciones específicas
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('d', lambda event: self.delete_task())
        self.root.bind('c', lambda event: self.complete_task())
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    # --- Lógica de la Aplicación ---

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)

            # Feedback visual: marcar como completada
            if not task.startswith("✔ "):
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {task}")
                self.tasks_listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para completar.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()