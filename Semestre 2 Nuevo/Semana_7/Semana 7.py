class Archivo:
    """
    Clase que demuestra el uso de constructores y destructores en Python.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor: se ejecuta automáticamente cuando se crea el objeto.
        Inicializa los atributos y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"Constructor: Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        if self.archivo:
            self.archivo.write(texto + "\n")
            print("Texto escrito en el archivo.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto es eliminado de la memoria.
        Se encarga de cerrar el archivo.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Destructor: Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    print("Inicio del programa")

    archivo1 = Archivo("ejemplo.txt")
    archivo1.escribir("Hola, este es un ejemplo de constructores y destructores.")
    archivo1.escribir("Python maneja automáticamente la memoria.")

    # Eliminamos el objeto de forma explícita
    del archivo1

    print("Fin del programa")
