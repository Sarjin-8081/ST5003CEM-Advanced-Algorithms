import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])

    def get_vertices(self):
        return list(self.adj_list.keys())

    # --- 1. Dijkstra's Algorithm ---
    def dijkstra(self, start, target):
        distances = {v: float('inf') for v in self.adj_list}
        distances[start] = 0
        predecessors = {v: None for v in self.adj_list}
        
        # Min-Priority Queue stores (distance, vertex)
        pq = [(0, start)]
        
        while pq:
            curr_dist, u = heapq.heappop(pq)
            
            if u == target:
                break
            if curr_dist > distances[u]:
                continue
                
            for v, weight in self.get_neighbors(u):
                # Dijkstra handles non-negative paths
                new_dist = curr_dist + max(0, weight) 
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heapq.heappush(pq, (new_dist, v))
                    
        # Reconstruct path
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = predecessors[curr]
        path.reverse()
        
        return path if path[0] == start else [], distances[target]

    # --- 2. Prim's Algorithm (MST) ---
    def prim(self, start):
        mst_edges = []
        visited = set([start])
        pq = []
        
        # Push all edges leaving the start vertex into min-heap
        for neighbor, weight in self.get_neighbors(start):
            heapq.heappush(pq, (weight, start, neighbor))
            
        total_cost = 0
        while pq and len(visited) < len(self.adj_list):
            weight, u, v = heapq.heappop(pq)
            
            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))
                total_cost += weight
                
                for neighbor, next_weight in self.get_neighbors(v):
                    if neighbor not in visited:
                        heapq.heappush(pq, (next_weight, v, neighbor))
                        
        return mst_edges, total_cost

    # --- 3. Bellman-Ford Algorithm (with Negative Cycle Detection) ---
    def bellman_ford(self, start, target):
        distances = {v: float('inf') for v in self.adj_list}
        distances[start] = 0
        predecessors = {v: None for v in self.adj_list}
        vertices = self.get_vertices()
        
        # Relax edges |V| - 1 times
        for _ in range(len(vertices) - 1):
            for u in vertices:
                for v, weight in self.get_neighbors(u):
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        predecessors[v] = u
                        
        # Check for negative-weight cycles
        for u in vertices:
            for v, weight in self.get_neighbors(u):
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    # Negative cycle detected!
                    return "NEGATIVE_CYCLE", None
                    
        # Reconstruct path
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = predecessors[curr]
        path.reverse()
        
        return path if path[0] == start else [], distances[target]