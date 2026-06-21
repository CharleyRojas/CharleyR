import tkinter as tk
from tkinter import messagebox, ttk
import json
import os


# 1. REGISTRO / ESTRUCTURA DE DATOS (POO)
class Paciente:
    def __init__(self, nombre, edad, sintoma):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma

    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "sintoma": self.sintoma}

    @staticmethod
    def from_dict(data):
        if data is None: return None
        return Paciente(data["nombre"], data["edad"], data["sintoma"])


# 2. CLASE DE GESTIÓN (Estructuras de Datos y Archivos)
class GestionClinica:
    def __init__(self):
        self.archivo_datos = "agenda_datos.json"
        self.horas = ["08:00", "09:00", "10:00"]
        self.especialidades = ["General", "Pediatria", "Cardiologia"]

        # VECTOR lineal de pacientes e historial
        self.vector_pacientes = []
        # MATRIZ bidimensional de turnos (3x3)
        self.matriz_turnos = [[None for _ in range(3)] for _ in range(3)]

        self.cargar_datos()

    def agendar_turno(self, nombre, edad, sintoma, index_hora, index_esp):
        if self.matriz_turnos[index_hora][index_esp] is not None:
            return False, "Ese horario y especialidad ya están ocupados."

        nuevo = Paciente(nombre, edad, sintoma)
        self.vector_pacientes.append(nuevo)
        self.matriz_turnos[index_hora][index_esp] = nuevo
        self.guardar_datos()
        return True, "Turno agendado con éxito."

    def guardar_datos(self):
        # Convertimos las estructuras de datos a un formato JSON compatible
        matriz_serializada = []
        for fila in self.matriz_turnos:
            fila_serializada = [p.to_dict() if p else None for p in fila]
            matriz_serializada.append(fila_serializada)

        vector_serializado = [p.to_dict() for p in self.vector_pacientes]

        datos = {
            "vector": vector_serializado,
            "matriz": matriz_serializada
        }
        with open(self.archivo_datos, "w") as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        if not os.path.exists(self.archivo_datos):
            return  # Si no existe el archivo, inicia vacío

        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)

            self.vector_pacientes = [Paciente.from_dict(p) for p in datos.get("vector", [])]

            matriz_raw = datos.get("matriz", [])
            for i in range(len(matriz_raw)):
                for j in range(len(matriz_raw[i])):
                    if matriz_raw[i][j]:
                        self.matriz_turnos[i][j] = Paciente.from_dict(matriz_raw[i][j])
        except Exception as e:
            print("Error al cargar datos antiguos:", e)


# 3. INTERFAZ GRÁFICA DE USUARIO (GUI)
class AppClinica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión Clínica - Semana 4")
        self.geometry("750x600")
        self.backend = GestionClinica()

        self.crear_componentes()
        self.actualizar_tabla_matriz()

    def crear_componentes(self):
        # --- Formulario de Registro ---
        frame_form = tk.LabelFrame(self, text=" Registrar Nuevo Paciente y Turno ", padx=10, pady=10)
        frame_form.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, pady=2, padx=5)

        tk.Label(frame_form, text="Edad:").grid(row=0, column=2, sticky="w", pady=2)
        self.entry_edad = tk.Entry(frame_form, width=10)
        self.entry_edad.grid(row=0, column=3, pady=2, padx=5)

        tk.Label(frame_form, text="Síntoma:").grid(row=1, column=0, sticky="w", pady=2)
        self.entry_sintoma = tk.Entry(frame_form, width=30)
        self.entry_sintoma.grid(row=1, column=1, pady=2, padx=5)

        tk.Label(frame_form, text="Hora:").grid(row=2, column=0, sticky="w", pady=5)
        self.combo_hora = ttk.Combobox(frame_form, values=self.backend.horas, state="readonly", width=12)
        self.combo_hora.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        self.combo_hora.current(0)

        tk.Label(frame_form, text="Especialidad:").grid(row=2, column=2, sticky="w", pady=5)
        self.combo_esp = ttk.Combobox(frame_form, values=self.backend.especialidades, state="readonly", width=15)
        self.combo_esp.grid(row=2, column=3, sticky="w", padx=5, pady=5)
        self.combo_esp.current(0)

        btn_registrar = tk.Button(frame_form, text="Guardar y Agendar", bg="#4CAF50", fg="white",
                                  command=self.procesar_registro)
        btn_registrar.grid(row=2, column=4, padx=15, pady=5)

        # --- SECCIÓN REPORTERÍA 1: VISUALIZAR MATRIZ ---
        frame_matriz = tk.LabelFrame(self, text=" Reportería: Matriz de Turnos (Visualización General) ", padx=10,
                                     pady=10)
        frame_matriz.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("hora", "general", "pediatria", "cardiologia")
        self.tabla_matriz = ttk.Treeview(frame_matriz, columns=columnas, show="headings", height=4)
        self.tabla_matriz.heading("hora", text="Hora")
        self.tabla_matriz.heading("general", text="General")
        self.tabla_matriz.heading("pediatria", text="Pediatría")
        self.tabla_matriz.heading("cardiologia", text="Cardiología")

        self.tabla_matriz.column("hora", width=80, anchor="center")
        self.tabla_matriz.column("general", width=180, anchor="center")
        self.tabla_matriz.column("pediatria", width=180, anchor="center")
        self.tabla_matriz.column("cardiologia", width=180, anchor="center")
        self.tabla_matriz.pack(fill="both", expand=True)

        # --- SECCIÓN REPORTERÍA 2: CONSULTAR ELEMENTO ---
        frame_consulta = tk.LabelFrame(self, text=" Reportería: Consultar Registro Específico ", padx=10, pady=10)
        frame_consulta.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_consulta, text="Buscar Paciente por Nombre:").pack(side="left", padx=5)
        self.entry_buscar = tk.Entry(frame_consulta, width=25)
        self.entry_buscar.pack(side="left", padx=5)

        btn_buscar = tk.Button(frame_consulta, text="Consultar", bg="#008CBA", fg="white",
                               command=self.procesar_consulta)
        btn_buscar.pack(side="left", padx=5)

    def actualizar_tabla_matriz(self):
        # Limpiamos la tabla visual
        for i in self.tabla_matriz.get_children():
            self.tabla_matriz.delete(i)

        # Rellenamos recorriendo la MATRIZ del backend
        for i, hora in enumerate(self.backend.horas):
            fila_valores = [hora]
            for j in range(3):
                paciente = self.backend.matriz_turnos[i][j]
                if paciente:
                    fila_valores.append(paciente.nombre)
                else:
                    fila_valores.append("[ Disponible ]")
            self.tabla_matriz.insert("", "end", values=fila_valores)

    def procesar_registro(self):
        nombre = self.entry_nombre.get().strip()
        sintoma = self.entry_sintoma.get().strip()

        if not nombre or not sintoma or not self.entry_edad.get():
            messagebox.showwarning("Campos Vacíos", "Por favor, llena todos los campos.")
            return

        try:
            edad = int(self.entry_edad.get())
        except ValueError:
            messagebox.showerror("Error de Tipo", "La edad debe ser un número entero.")
            return

        idx_hora = self.combo_hora.current()
        idx_esp = self.combo_esp.current()

        exito, msg = self.backend.agendar_turno(nombre, edad, sintoma, idx_hora, idx_esp)

        if exito:
            messagebox.showinfo("Éxito", msg)
            self.actualizar_tabla_matriz()
            # Limpiar formulario
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)
            self.entry_sintoma.delete(0, tk.END)
        else:
            messagebox.showerror("Error de Estructura", msg)

    def procesar_consulta(self):
        nombre_buscar = self.entry_buscar.get().strip().lower()
        if not nombre_buscar:
            messagebox.showwarning("Atención", "Escribe un nombre para buscar.")
            return

        encontrado = False
        # Buscamos en el VECTOR de la estructura
        for paciente in self.backend.vector_pacientes:
            if paciente.nombre.lower() == nombre_buscar:
                # Si lo encuentra, busca en qué celda de la MATRIZ quedó guardado
                info_turno = "No asignado en matriz"
                for f in range(3):
                    for c in range(3):
                        if self.backend.matriz_turnos[f][c] == paciente:
                            info_turno = f"Hora: {self.backend.horas[f]} | Especialidad: {self.backend.especialidades[c]}"

                detalles = f"Nombre: {paciente.nombre}\nEdad: {paciente.edad} años\nSíntoma: {paciente.sintoma}\n\nUbicación Estructura:\n{info_turno}"
                messagebox.showinfo("Elemento Consultado", detalles)
                encontrado = True
                break

        if not encontrado:
            messagebox.showinfo("Resultado", "No se encontró ningún registro con ese nombre.")


if __name__ == "__main__":
    app = AppClinica()
    app.mainloop()