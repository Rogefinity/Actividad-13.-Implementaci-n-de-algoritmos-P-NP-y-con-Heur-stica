from pydantic import BaseModel
from typing import Dict

class GrafoGeneradoInput(BaseModel):
    nodos: int
    peso_min: int = 1
    peso_max: int = 100

class AlgoritmoInput(BaseModel):
    #diccionario de adyacencia
    grafo: Dict[str, Dict[str, float]]
    origen: str = "0"
    destino: str = "1" 
