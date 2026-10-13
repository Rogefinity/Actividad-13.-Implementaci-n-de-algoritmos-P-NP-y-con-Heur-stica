# Actividad 13. Implementación de algoritmos P, NP y con Heurística
**Estudiante:** Rogelio Sotomayor Carrasco
**No. de cuenta:** 195721

## 1. Documentación de Algoritmos Implementados

### 1.1. Camino Mínimo (Dijkstra) - Clase P
*   **Complejidad:** $O(\vert{}E\vert{} \log \vert{}V\vert{})$
*   **Comportamiento:** Algoritmo determinista y polinómico. Escala de manera eficiente incluso con miles de nodos al utilizar una cola de prioridad (`heapq`). Encuentra matemáticamente el camino más corto hacia el destino garantizado.

### 1.2. Agente Viajero Exacto (Fuerza Bruta) - Clase NP-Completo
*   **Complejidad:** $O(n!)$
*   **Comportamiento:** Intratable. Verifica cada ciclo hamiltoniano posible mediante permutaciones. Para $n$ nodos, explora $(n-1)!$ combinaciones. Funciona de manera óptima para grafos pequeños ($n \le 10$), pero experimenta una "explosión factorial" que agota el tiempo y la memoria para grafos medianos y grandes.

### 1.3. Agente Viajero (Heurística Voraz / Vecino más cercano)
*   **Complejidad:** $O(n^2)$
*   **Comportamiento:** Polinómico pero subóptimo. En cada paso toma la decisión localmente más barata. Sacrifica la precisión (no garantiza el costo mínimo) a cambio de una ejecución instantánea y un uso mínimo de memoria, salvando la barrera del NP-Completo.

---

## 2. Pruebas de Ejecución en Grafos Sintéticos

Se generaron grafos completos sintéticos utilizando el endpoint `/api/generar_grafo` con pesos aleatorios entre 1 y 100. A continuación, los resultados devueltos por el servidor.

### Prueba 1: Grafo de 5 Nodos
*   **Dijkstra:** 
    * Tiempo: 0.012 ms | Memoria: 840 bytes | Nodos evaluados: 5 | Costo: 45
*   **TSP (Fuerza Bruta Exacta):** 
    * Tiempo: 0.065 ms | Memoria: 1,120 bytes | Nodos evaluados: 24 permutaciones | Costo: 184
*   **TSP (Heurística Voraz):** 
    * Tiempo: 0.018 ms | Memoria: 520 bytes | Nodos recorridos: 5 | Costo: 210 (Margen de error empírico)

### Prueba 2: Grafo de 10 Nodos
*   **Dijkstra:** 
    * Tiempo: 0.021 ms | Memoria: 1,210 bytes | Nodos evaluados: 10 | Costo: 68
*   **TSP (Fuerza Bruta Exacta):** 
    * Tiempo: 345.8 ms | Memoria: 2,840 bytes | Nodos evaluados: 362,880 permutaciones | Costo: 156
*   **TSP (Heurística Voraz):** 
    * Tiempo: 0.031 ms | Memoria: 800 bytes | Nodos recorridos: 10 | Costo: 232

### Prueba 3: Grafo de 15 Nodos (La pared de la Intratabilidad)
*   **Dijkstra:** 
    * Tiempo: 0.035 ms | Memoria: 1,850 bytes | Nodos evaluados: 15 | Costo: 82
*   **TSP (Fuerza Bruta Exacta):** 
    * Tiempo: **ABORTADO (Exceso de Tiempo)**. 
    * *Análisis:* Para 15 nodos, el algoritmo debe evaluar $14!$ (87,178,291,200) permutaciones. A la tasa de procesamiento de la prueba de 10 nodos, esto tardaría más de **24 horas de cómputo ininterrumpido**, demostrando en la práctica los límites físicos de la computación ante la Clase NP. El backend cortó la ejecución por límite de seguridad ($>5M$ evaluaciones).
*   **TSP (Heurística Voraz):** 
    * Tiempo: 0.051 ms | Memoria: 1,100 bytes | Nodos recorridos: 15 | Costo: 315

### Conclusión
Se observó exitosamente la tasa de crecimiento. Dijkstra y la Heurística Voraz (Clase P y O(n^2)) respondieron en fracciones de milisegundo independientemente del crecimiento de $n$. En contraste, la solución exacta del Agente Viajero (Clase NP) pasó de $0.065$ ms en 5 nodos a volverse computacionalmente intratable con apenas 15 nodos.

