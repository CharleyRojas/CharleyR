import tkinter as tk
from tkinter import ttk, messagebox


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal - Versión Estándar")
        self.root.geometry("650x500")

        # --- CONTENEDOR DE ENTRADA (Frames) ---
        frame_entrada = tk.LabelFrame(self.root, text="Detalles del Nuevo Evento", padx=10, pady=10)
        frame_entrada.pack(fill="x", padx=15, pady=10)

        # Campos para la Fecha (Día, Mes, Año)
        tk.Label(frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0, sticky="w")

        # Usamos un Frame pequeño para agrupar los campos de fecha
        f_fecha = tk.Frame(frame_entrada)
        f_fecha.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.ent_dia = tk.Spinbox(f_fecha, from_=1, to=31, width=3)
        self.ent_dia.pack(side="left")
        tk.Label(f_fecha, text="/").pack(side="left")
        self.ent_mes = tk.Spinbox(f_fecha, from_=1, to=12, width=3)
        self.ent_mes.pack(side="left")
        tk.Label(f_fecha, text="/").pack(side="left")
        self.ent_anio = tk.Entry(f_fecha, width=5)
        self.ent_anio.insert(0, "2026")
        self.ent_anio.pack(side="left")

        # Campo para la Hora
        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=(15, 0))
        self.ent_hora = tk.Entry(frame_entrada, width=10)
        self.ent_hora.insert(0, "12:00")
        self.ent_hora.grid(row=0, column=3, padx=5, pady=5)

        # Campo para la Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.ent_desc = tk.Entry(frame_entrada, width=55)
        self.ent_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # --- CONTENEDOR DE VISUALIZACIÓN (TreeView) ---
        frame_lista = tk.LabelFrame(self.root, text="Eventos Programados")
        frame_lista.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")

        # Configurar encabezados
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Ajustar ancho de columnas
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=350)

        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrolly = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrolly.set)
        scrolly.pack(side="right", fill="y")

        # --- CONTENEDOR DE ACCIONES (Botones) ---
        frame_acciones = tk.Frame(self.root)
        frame_acciones.pack(fill="x", padx=15, pady=15)

        btn_agregar = tk.Button(frame_acciones, text="➕ Agregar Evento",
                                command=self.agregar_evento, bg="#d4edda", width=15)
        btn_agregar.pack(side="left", padx=5)

        btn_eliminar = tk.Button(frame_acciones, text="🗑️ Eliminar Seleccionado",
                                 command=self.eliminar_evento, bg="#f8d7da", width=20)
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = tk.Button(frame_acciones, text="Salir", command=self.root.destroy)
        btn_salir.pack(side="right", padx=5)

    def agregar_evento(self):
        # Construir la fecha desde los campos
        fecha_full = f"{self.ent_dia.get()}/{self.ent_mes.get()}/{self.ent_anio.get()}"
        hora = self.ent_hora.get()
        desc = self.ent_desc.get()

        if hora and desc:
            self.tree.insert("", "end", values=(fecha_full, hora, desc))
            # Limpiar descripción para el siguiente
            self.ent_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            # Requisito opcional: Diálogo de confirmación
            respuesta = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
            if respuesta:
                self.tree.delete(seleccion)
        else:
            messagebox.showwarning("Atención", "Selecciona un evento de la lista para eliminarlo.")


if __name__ == "__main__":
    app_root = tk.Tk()
    mi_agenda = AgendaApp(app_root)
    app_root.mainloop()