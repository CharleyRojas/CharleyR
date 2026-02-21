class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Usamos __ para indicar atributos privados (encapsulamiento)
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters
    def get_id(self): return self.__id

    def get_nombre(self): return self.__nombre

    def set_nombre(self, nombre): self.__nombre = nombre

    def get_cantidad(self): return self.__cantidad

    def set_cantidad(self, cantidad): self.__cantidad = cantidad

    def get_precio(self): return self.__precio

    def set_precio(self, precio): self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Stock: {self.__cantidad} | Precio: ${self.__precio}"