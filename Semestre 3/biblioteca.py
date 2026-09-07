"""
Sistema de Registro de Libros en una Biblioteca
Guia de Practicas N.3 - Estructura de Datos - UEA
Estructuras utilizadas: conjuntos (set), mapas/diccionarios (dict)
"""

import time
import random
from collections import defaultdict

class Biblioteca:
    def __init__(self):
        # MAPA (dict): isbn -> datos del libro {titulo, autor, categoria, disponible}
        self.catalogo = {}
        # CONJUNTO (set): ISBNs unicos registrados, evita duplicados automaticamente
        self.isbns_registrados = set()
        # CONJUNTO (set): categorias unicas presentes en la biblioteca
        self.categorias = set()
        # MAPA de CONJUNTOS: categoria -> {isbn1, isbn2, ...}
        self.indice_categoria = defaultdict(set)
        # MAPA de CONJUNTOS: autor -> {isbn1, isbn2, ...}
        self.indice_autor = defaultdict(set)
        # CONJUNTO (set): isbns actualmente prestados
        self.prestados = set()

    def registrar_libro(self, isbn, titulo, autor, categoria):
        if isbn in self.isbns_registrados:
            print(f"  [AVISO] El ISBN {isbn} ya existe. No se registra duplicado.")
            return False
        self.isbns_registrados.add(isbn)
        self.catalogo[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "disponible": True
        }
        self.categorias.add(categoria)
        self.indice_categoria[categoria].add(isbn)
        self.indice_autor[autor].add(isbn)
        return True

    def prestar_libro(self, isbn):
        if isbn not in self.catalogo:
            print(f"  [ERROR] ISBN {isbn} no encontrado.")
            return False
        if isbn in self.prestados:
            print(f"  [AVISO] El libro '{self.catalogo[isbn]['titulo']}' ya esta prestado.")
            return False
        self.prestados.add(isbn)
        self.catalogo[isbn]["disponible"] = False
        return True

    def devolver_libro(self, isbn):
        if isbn in self.prestados:
            self.prestados.discard(isbn)
            self.catalogo[isbn]["disponible"] = True
            return True
        return False

    def buscar_por_isbn(self, isbn):
        # Acceso O(1) gracias al mapa/diccionario
        return self.catalogo.get(isbn)

    def libros_por_categoria(self, categoria):
        # Consulta O(1) sobre el mapa de conjuntos
        return self.indice_categoria.get(categoria, set())

    def libros_por_autor(self, autor):
        return self.indice_autor.get(autor, set())

    def libros_disponibles(self):
        return {isbn for isbn in self.catalogo if self.catalogo[isbn]["disponible"]}

    def categorias_en_comun(self, otra_biblioteca):
        # Operacion de CONJUNTOS: interseccion
        return self.categorias & otra_biblioteca.categorias

    def reporte_general(self):
        print("=" * 70)
        print("REPORTE GENERAL DE LA BIBLIOTECA")
        print("=" * 70)
        print(f"Total de libros registrados : {len(self.catalogo)}")
        print(f"Total de categorias unicas   : {len(self.categorias)} -> {sorted(self.categorias)}")
        print(f"Libros prestados actualmente : {len(self.prestados)}")
        print(f"Libros disponibles           : {len(self.libros_disponibles())}")
        print("-" * 70)
        print(f"{'ISBN':<16}{'Titulo':<28}{'Autor':<20}{'Categoria':<14}{'Estado'}")
        print("-" * 70)
        for isbn, datos in self.catalogo.items():
            estado = "Disponible" if datos["disponible"] else "Prestado"
            print(f"{isbn:<16}{datos['titulo'][:26]:<28}{datos['autor'][:18]:<20}{datos['categoria']:<14}{estado}")
        print("=" * 70)


def analizar_tiempos_busqueda():
    """Compara el tiempo de busqueda en un dict (mapa/hash) vs una lista."""
    n = 50000
    claves = [f"978-{i:010d}" for i in range(n)]
    valores = {c: f"Libro {i}" for i, c in enumerate(claves)}
    lista_equivalente = list(valores.items())

    objetivo = claves[-1]  # peor caso para la lista: al final

    inicio = time.perf_counter()
    _ = valores.get(objetivo)
    t_dict = time.perf_counter() - inicio

    inicio = time.perf_counter()
    _ = next((v for k, v in lista_equivalente if k == objetivo), None)
    t_lista = time.perf_counter() - inicio

    print("\nANALISIS DE TIEMPO DE EJECUCION (busqueda de 1 elemento en n=%d)" % n)
    print(f"  Busqueda en diccionario (mapa/hash) -> {t_dict*1e6:.3f} microsegundos  (O(1) promedio)")
    print(f"  Busqueda en lista (recorrido lineal) -> {t_lista*1e6:.3f} microsegundos  (O(n))")
    if t_dict > 0:
        print(f"  El diccionario fue aproximadamente {t_lista/t_dict:.1f} veces mas rapido.")
    return t_dict, t_lista


if __name__ == "__main__":
    biblioteca = Biblioteca()

    libros = [
        ("978-0134685991", "Effective Java", "Joshua Bloch", "Programacion"),
        ("978-8441536041", "Cien anios de soledad", "Gabriel Garcia Marquez", "Literatura"),
        ("978-0262033848", "Introduction to Algorithms", "Thomas Cormen", "Algoritmos"),
        ("978-8437604947", "Don Quijote de la Mancha", "Miguel de Cervantes", "Literatura"),
        ("978-1491957660", "Python de alto rendimiento", "Micha Gorelick", "Programacion"),
        ("978-9978674097", "Historia del Ecuador", "Enrique Ayala Mora", "Historia"),
        ("978-0134685991", "Effective Java (duplicado)", "Joshua Bloch", "Programacion"),
    ]

    print("REGISTRANDO LIBROS EN LA BIBLIOTECA")
    print("-" * 70)
    for isbn, titulo, autor, categoria in libros:
        ok = biblioteca.registrar_libro(isbn, titulo, autor, categoria)
        if ok:
            print(f"  [OK] Registrado: {titulo} ({autor}) - {categoria}")

    print()
    biblioteca.prestar_libro("978-8441536041")
    biblioteca.prestar_libro("978-0262033848")

    biblioteca.reporte_general()

    print("\nCONSULTA POR CATEGORIA: 'Literatura'")
    for isbn in biblioteca.libros_por_categoria("Literatura"):
        print(f"  -> {biblioteca.catalogo[isbn]['titulo']}")

    print("\nCONSULTA POR AUTOR: 'Joshua Bloch'")
    for isbn in biblioteca.libros_por_autor("Joshua Bloch"):
        print(f"  -> {biblioteca.catalogo[isbn]['titulo']}")

    print("\nLIBROS ACTUALMENTE DISPONIBLES:")
    for isbn in biblioteca.libros_disponibles():
        print(f"  -> {biblioteca.catalogo[isbn]['titulo']}")

    # Ejemplo de interseccion de conjuntos entre dos sucursales
    sucursal_2 = Biblioteca()
    sucursal_2.registrar_libro("978-0000000001", "Rayuela", "Julio Cortazar", "Literatura")
    sucursal_2.registrar_libro("978-0000000002", "Clean Code", "Robert C. Martin", "Programacion")
    comunes = biblioteca.categorias_en_comun(sucursal_2)
    print(f"\nCATEGORIAS EN COMUN ENTRE SUCURSAL CENTRAL Y SUCURSAL 2 (interseccion de conjuntos): {comunes}")

    analizar_tiempos_busqueda()
