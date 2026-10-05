"""
Practica #04 - Estructura de Datos (UEA)
Encuentro de vuelos baratos con un GRAFO dirigido y ponderado.

Estructura usada : lista de adyacencia (dict[str, list[Vuelo]])
Algoritmos       : Dijkstra con cola de prioridad (heapq) y BFS (minimo de escalas)
Base de datos    : archivo de texto 'vuelos.txt' (ficticia)
Autor            : Charley Fernando Rojas Andrade
"""
import heapq
import sys
import time
from collections import deque, namedtuple

Vuelo = namedtuple("Vuelo", "origen destino aerolinea precio duracion")

AEROPUERTOS = {
    "UIO": "Quito", "GYE": "Guayaquil", "CUE": "Cuenca", "BOG": "Bogota",
    "MDE": "Medellin", "LIM": "Lima", "SCL": "Santiago", "EZE": "Buenos Aires",
    "PTY": "Panama", "MIA": "Miami", "MAD": "Madrid",
}


class GrafoVuelos:
    """Grafo dirigido ponderado con lista de adyacencia."""

    def __init__(self):
        self.adyacencia = {}          # codigo -> lista de Vuelo salientes

    # ---------- carga ----------
    def agregar_vuelo(self, v):
        self.adyacencia.setdefault(v.origen, []).append(v)
        self.adyacencia.setdefault(v.destino, [])

    def cargar_archivo(self, ruta):
        with open(ruta, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                o, d, a, p, t = linea.split(",")
                self.agregar_vuelo(Vuelo(o, d, a, float(p), int(t)))

    # ---------- reporteria ----------
    def total_vuelos(self):
        return sum(len(l) for l in self.adyacencia.values())

    def reporte_aeropuertos(self):
        print(f"{'COD':<5}{'CIUDAD':<15}{'SALIDAS':>8}{'LLEGADAS':>10}")
        llegadas = {k: 0 for k in self.adyacencia}
        for lista in self.adyacencia.values():
            for v in lista:
                llegadas[v.destino] += 1
        for cod in sorted(self.adyacencia):
            print(f"{cod:<5}{AEROPUERTOS.get(cod, '-'):<15}"
                  f"{len(self.adyacencia[cod]):>8}{llegadas[cod]:>10}")

    def reporte_vuelos(self, origen=None):
        print(f"{'ORIGEN':<8}{'DESTINO':<9}{'AEROLINEA':<16}{'PRECIO':>8}{'MIN':>6}")
        for cod in sorted(self.adyacencia):
            if origen and cod != origen:
                continue
            for v in sorted(self.adyacencia[cod], key=lambda x: x.precio):
                print(f"{v.origen:<8}{v.destino:<9}{v.aerolinea:<16}"
                      f"{v.precio:>8.2f}{v.duracion:>6}")

    def reporte_estadistico(self):
        todos = [v for l in self.adyacencia.values() for v in l]
        barato = min(todos, key=lambda v: v.precio)
        caro = max(todos, key=lambda v: v.precio)
        prom = sum(v.precio for v in todos) / len(todos)
        print(f"Aeropuertos (vertices): {len(self.adyacencia)}")
        print(f"Vuelos (aristas)      : {len(todos)}")
        print(f"Precio promedio       : ${prom:.2f}")
        print(f"Vuelo mas barato      : {barato.origen}->{barato.destino} ${barato.precio:.2f}")
        print(f"Vuelo mas caro        : {caro.origen}->{caro.destino} ${caro.precio:.2f}")

    # ---------- algoritmos ----------
    def ruta_mas_barata(self, origen, destino, criterio="precio"):
        """Dijkstra. criterio: 'precio' o 'duracion'. Retorna (costo, [vuelos])."""
        if origen not in self.adyacencia or destino not in self.adyacencia:
            raise KeyError("Aeropuerto inexistente")
        dist = {origen: 0}
        previo = {}
        cola = [(0, origen)]
        visitados = set()
        while cola:
            costo, u = heapq.heappop(cola)
            if u in visitados:
                continue
            visitados.add(u)
            if u == destino:
                break
            for v in self.adyacencia[u]:
                peso = v.precio if criterio == "precio" else v.duracion
                nuevo = costo + peso
                if nuevo < dist.get(v.destino, float("inf")):
                    dist[v.destino] = nuevo
                    previo[v.destino] = v
                    heapq.heappush(cola, (nuevo, v.destino))
        if destino not in dist:
            return None, []
        ruta, actual = [], destino
        while actual != origen:
            vuelo = previo[actual]
            ruta.append(vuelo)
            actual = vuelo.origen
        ruta.reverse()
        return dist[destino], ruta

    def menos_escalas(self, origen, destino):
        """BFS: ruta con el menor numero de vuelos."""
        cola = deque([origen])
        previo = {origen: None}
        while cola:
            u = cola.popleft()
            if u == destino:
                break
            for v in self.adyacencia[u]:
                if v.destino not in previo:
                    previo[v.destino] = v
                    cola.append(v.destino)
        if destino not in previo:
            return []
        ruta, actual = [], destino
        while previo[actual] is not None:
            ruta.append(previo[actual])
            actual = previo[actual].origen
        ruta.reverse()
        return ruta


def mostrar_ruta(titulo, ruta):
    print(f"\n{titulo}")
    if not ruta:
        print("  No existe ruta.")
        return
    print("  " + " -> ".join([ruta[0].origen] + [v.destino for v in ruta]))
    for v in ruta:
        print(f"    {v.origen}->{v.destino}  {v.aerolinea:<15} ${v.precio:>7.2f}  {v.duracion} min")
    print(f"  TOTAL: ${sum(v.precio for v in ruta):.2f} | "
          f"{sum(v.duracion for v in ruta)} min | {len(ruta)-1} escala(s)")


def principal():
    g = GrafoVuelos()
    g.cargar_archivo("vuelos.txt")

    print("=" * 60)
    print(" SISTEMA DE VUELOS BARATOS - GRAFO DIRIGIDO PONDERADO")
    print("=" * 60)
    print("\n[1] REPORTE ESTADISTICO"); g.reporte_estadistico()
    print("\n[2] REPORTE DE AEROPUERTOS"); g.reporte_aeropuertos()
    print("\n[3] VUELOS DESDE UIO (ordenados por precio)"); g.reporte_vuelos("UIO")

    consultas = [("UIO", "MAD"), ("GYE", "EZE"), ("CUE", "MIA"), ("MDE", "SCL")]
    print("\n[4] CONSULTAS DE RUTA MAS BARATA (Dijkstra)")
    for o, d in consultas:
        costo, ruta = g.ruta_mas_barata(o, d)
        mostrar_ruta(f"{o} ({AEROPUERTOS[o]}) a {d} ({AEROPUERTOS[d]})", ruta)

    print("\n[5] COMPARACION: MAS BARATA vs MAS RAPIDA vs MENOS ESCALAS (UIO -> MAD)")
    mostrar_ruta("Mas barata", g.ruta_mas_barata("UIO", "MAD", "precio")[1])
    mostrar_ruta("Mas rapida", g.ruta_mas_barata("UIO", "MAD", "duracion")[1])
    mostrar_ruta("Menos escalas (BFS)", g.menos_escalas("UIO", "MAD"))


def medir_tiempos():
    g = GrafoVuelos(); g.cargar_archivo("vuelos.txt")
    codigos = sorted(g.adyacencia)
    pares = [(o, d) for o in codigos for d in codigos if o != d]
    REP = 200
    t0 = time.perf_counter()
    for _ in range(REP):
        for o, d in pares:
            g.ruta_mas_barata(o, d)
    total = time.perf_counter() - t0
    print(f"Pares origen-destino evaluados : {len(pares)}")
    print(f"Repeticiones                   : {REP}")
    print(f"Tiempo total                   : {total:.3f} s")
    print(f"Tiempo promedio por consulta   : {total/(REP*len(pares))*1e6:.1f} microsegundos")
    t0 = time.perf_counter(); g2 = GrafoVuelos(); g2.cargar_archivo("vuelos.txt")
    print(f"Tiempo de carga del archivo    : {(time.perf_counter()-t0)*1e3:.3f} ms")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "tiempos":
        medir_tiempos()
    else:
        principal()
