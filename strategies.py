# --- 1. Dynamic Programming: Matrix Chain Multiplication ---
def matrix_chain_order(p):
    n = len(p) - 1
    # m[i][j] stores the minimum scalar multiplications needed
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # Recurrence relation implementation
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n]


# --- 2. Greedy Algorithm: Minimum Number of Platforms ---
def find_minimum_platforms(arrival, departure):
    # Sort arrival and departure vectors chronologically
    arrival.sort()
    departure.sort()
    
    platforms_needed = 1
    max_platforms = 1
    
    i = 1  # Pointer for arrival times
    j = 0  # Pointer for departure times
    
    while i < len(arrival) and j < len(departure):
        # If a train arrives before the previous one leaves, allocate a platform
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
        else:
            # A train left, freeing up a platform slot
            platforms_needed -= 1
            j += 1
            
        if platforms_needed > max_platforms:
            max_platforms = platforms_needed
            
    return max_platforms


# --- 3. Backtracking: Hamiltonian Cycle Solver with Pruning ---
class HamiltonianSolver:
    def __init__(self, adjacency_matrix):
        self.graph = adjacency_matrix
        self.V = len(adjacency_matrix)
        self.path = []

    def _is_safe(self, v, pos, path):
        # Pruning Check 1: Check if this vertex is an adjacent neighbor
        if self.graph[path[pos - 1]][v] == 0:
            return False
            
        # Pruning Check 2: Check if the vertex has already been visited
        if v in path:
            return False
            
        return True

    def _solve_util(self, path, pos):
        # Base case: All vertices are included in the path
        if pos == self.V:
            # Check if there is an edge from the last vertex back to the start
            return self.graph[path[pos - 1]][path[0]] == 1
            
        for v in range(1, self.V):
            if self._is_safe(v, pos, path):
                path[pos] = v
                
                # Recursive optimization step
                if self._solve_util(path, pos + 1):
                    return True
                    
                # Backtrack pruning step if path choice leads to a dead end
                path[pos] = -1
                
        return False

    def find_cycle(self):
        self.path = [-1] * self.V
        self.path[0] = 0  # Set the initial start vertex to 0
        
        if not self._solve_util(self.path, 1):
            return None
        return self.path