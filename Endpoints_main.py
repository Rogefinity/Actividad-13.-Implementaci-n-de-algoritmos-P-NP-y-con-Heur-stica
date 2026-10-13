from fastapi import FastAPI
from schemas import GrafoGeneradoInput, AlgoritmoInput
from algoritmos_act13 import (
    generar_grafo_sintetico, 
    dijkstra_p, 
    tsp_fuerza_bruta_np, 
    tsp_heuristica_voraz
)

app = FastAPI(title="Actividad 13: Algoritmos P, NP y Heurísticas")

@app.post("/api/generar_grafo")
def endpoint_generar_grafo(datos: GrafoGeneradoInput):
    grafo = generar_grafo_sintetico(datos.nodos, datos.peso_min, datos.peso_max)
    return {"grafo_sintetico": grafo}

@app.post("/api/dijkstra")
def endpoint_dijkstra(datos: AlgoritmoInput):
    return dijkstra_p(datos.grafo, datos.origen, datos.destino)

@app.post("/api/tsp/exacto")
def endpoint_tsp_exacto(datos: AlgoritmoInput):
    return tsp_fuerza_bruta_np(datos.grafo, datos.origen)

@app.post("/api/tsp/heuristica")
def endpoint_tsp_heuristica(datos: AlgoritmoInput):
    return tsp_heuristica_voraz(datos.grafo, datos.origen)
