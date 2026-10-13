import time
import heapq
import itertools
import random
import tracemalloc

def generar_grafo_sintetico(n: int, peso_min: int, peso_max: int):
    """Genera un grafo completo aleatorio."""
    grafo = {str(i): {} for i in range(n)}
    for u in range(n):
        for v in range(n):
            if u != v:
                grafo[str(u)][str(v)] = float(random.randint(peso_min, peso_max))
    return grafo

def dijkstra_p(grafo: dict, origen: str, destino: str):
    """Algoritmo de Clase P: O(|E| log |V|)"""
    tracemalloc.start()
    t0 = time.perf_counter()

    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0
    pq = [(0, origen)]
    nodos_explorados = 0

    while pq:
        d_actual, u = heapq.heappop(pq)
        nodos_explorados += 1
        if u == destino:
            break
        if d_actual > dist[u]:
            continue
        for v, peso in grafo[u].items():
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                heapq.heappush(pq, (dist[v], v))

    t_ms = (time.perf_counter() - t0) * 1000
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "tiempo_ejecucion_ms": t_ms,
        "memoria_consumida_bytes": peak_memory,
        "no_nodos_recorridos": nodos_explorados,
        "costo_camino": dist[destino]
    }

def tsp_fuerza_bruta_np(grafo: dict, origen: str):
    """Algoritmo Exacto NP-Completo: O(n!)"""
    tracemalloc.start()
    t0 = time.perf_counter()

    nodos = list(grafo.keys())
    otros_nodos = [n for n in nodos if n != origen]
    costo_minimo = float('inf')
    permutaciones_evaluadas = 0

    #límite de seguridad para evitar colgar el servidor en la prueba de 15 nodos
    limite_seguridad = 5000000 

    for perm in itertools.permutations(otros_nodos):
        permutaciones_evaluadas += 1
        ruta = [origen] + list(perm) + [origen]
        costo_actual = sum(grafo[ruta[i]][ruta[i+1]] for i in range(len(nodos)))
        if costo_actual < costo_minimo:
            costo_minimo = costo_actual
            
        if permutaciones_evaluadas > limite_seguridad:
            costo_minimo = "Timeout: Exceso O(n!)"
            break

    t_ms = (time.perf_counter() - t0) * 1000
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "tiempo_ejecucion_ms": t_ms,
        "memoria_consumida_bytes": peak_memory,
        "no_nodos_recorridos": permutaciones_evaluadas,
        "costo_camino": costo_minimo
    }

def tsp_heuristica_voraz(grafo: dict, origen: str):
    """Heurística Constructiva (Vecino más cercano): O(n^2)"""
    tracemalloc.start()
    t0 = time.perf_counter()

    n = len(grafo)
    visitados = {origen}
    costo_total = 0
    actual = origen

    for _ in range(n - 1):
        siguiente = min(
            (v for v in grafo[actual] if v not in visitados),
            key=lambda v: grafo[actual][v]
        )
        costo_total += grafo[actual][siguiente]
        visitados.add(siguiente)
        actual = siguiente
        
    #regresar al origen para cerrar el ciclo
    costo_total += grafo[actual][origen]

    t_ms = (time.perf_counter() - t0) * 1000
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "tiempo_ejecucion_ms": t_ms,
        "memoria_consumida_bytes": peak_memory,
        "no_nodos_recorridos": len(visitados),
        "costo_camino": costo_total
    }
