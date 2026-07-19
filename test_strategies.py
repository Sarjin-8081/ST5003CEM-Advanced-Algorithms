from strategies import matrix_chain_order, find_minimum_platforms, HamiltonianSolver

print("=== Task 3 Verification Run ===")

# 1. Test Dynamic Programming (Matrix Chain Order)
matrix_dimensions = [40, 20, 30, 10, 30] # 4 Matrices of sizes 40x20, 20x30, 30x10, 10x30
min_mults = matrix_chain_order(matrix_dimensions)
print(f"1. DP Matrix Chain Multiplication Min Cost: {min_mults}")

# 2. Test Greedy Algorithm (Train Platform Allocation)
arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
platforms = find_minimum_platforms(arrivals, departures)
print(f"2. Greedy Minimum Station Platforms Needed: {platforms}")

# 3. Test Backtracking (Hamiltonian Cycle with Pruning)
# 5-node interconnected transit loop grid matrix
transit_grid = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
solver = HamiltonianSolver(transit_grid)
cycle_path = solver.find_cycle()
if cycle_path:
    formatted_path = " -> ".join(map(str, cycle_path + [cycle_path[0]]))
    print(f"3. Backtracking Hamiltonian Cycle Path: {formatted_path}")
else:
    print("3. Backtracking Hamiltonian Cycle: No complete circuit found.")