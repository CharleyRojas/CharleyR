import os
import subprocess
import sys


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
            return True
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return False


def ejecutar_codigo(ruta_script):
    try:
        python_exe = sys.executable
        if os.name == 'nt':
            # Ejecución limpia para Windows sin conflicto de comillas
            subprocess.Popen(['cmd', '/k', python_exe, ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', python_exe, ruta_script])
    except Exception as e:
        print(f"Error al ejecutar: {e}")


def mostrar_menu():
    # Se ubica en C:\Users\CharleyR\PycharmProjects\CharleyR
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\n" + "=" * 40)
        print("     DASHBOARD PROYECTO: CharleyR")
        print("=" * 40)

        # Lista carpetas de Semestre automáticamente
        items = [f.name for f in os.scandir(ruta_base) if f.is_dir() and 'Semestre' in f.name]
        items.sort()

        for i, item in enumerate(items, start=1):
            print(f"{i} - {item}")
        print("0 - Salir")

        eleccion = input("\nSelecciona un semestre: ")
        if eleccion == '0': break

        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(items):
                # Navegación recursiva
                menu_carpetas(os.path.join(ruta_base, items[idx]))
        except ValueError:
            print("Entrada no válida.")


def menu_carpetas(ruta):
    while True:
        sub_carpetas = [f.name for f in os.scandir(ruta) if f.is_dir()]
        sub_carpetas.sort()

        print(f"\n--- Ubicación: {os.path.basename(ruta)} ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Volver atrás")

        eleccion = input("\nSelecciona subcarpeta: ")
        if eleccion == '0': break

        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(sub_carpetas):
                menu_scripts(os.path.join(ruta, sub_carpetas[idx]))
        except ValueError:
            pass


def menu_scripts(ruta):
    while True:
        scripts = [f.name for f in os.scandir(ruta) if f.name.endswith('.py')]
        scripts.sort()

        print(f"\n--- Scripts en: {os.path.basename(ruta)} ---")
        for i, s in enumerate(scripts, start=1):
            print(f"{i} - {s}")
        print("0 - Volver | 9 - Menú Principal")

        eleccion = input("\nSelecciona script: ")
        if eleccion == '0': break
        if eleccion == '9': sys.exit()  # Opción rápida para cerrar todo

        try:
            idx = int(eleccion) - 1
            ruta_comp = os.path.join(ruta, scripts[idx])
            if mostrar_codigo(ruta_comp):
                if input("\n¿Ejecutar? (1: Sí / 0: No): ") == '1':
                    ejecutar_codigo(ruta_comp)
        except:
            pass


if __name__ == "__main__":
    mostrar_menu()