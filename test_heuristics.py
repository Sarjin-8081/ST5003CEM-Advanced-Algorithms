import time
from heuristics import Customer, greedy_vrptw, local_search_swap, calculate_total_distance

# Mock delivery grid: depot (id=0) at center + 5 customers with demands and time frames
data = [
    Customer(0, 0, 0, 0, 0, 100),       # Depot
    Customer(1, 2, 3, 20, 10, 40),      # Cust 1
    Customer(2, -1, 4, 30, 0, 50),      # Cust 2
    Customer(3, 5, 1, 10, 20, 60),      # Cust 3
    Customer(4, -3, -2, 40, 5, 30),     # Cust 4
    Customer(5, 1, -4, 20, 15, 80)      # Cust 5
]
capacity = 60

print("=== Running VRPTW Heuristic Evaluation ===")

# Run Greedy Construction
t0 = time.perf_counter()
greedy_routes = greedy_vrptw(data, capacity)
t1 = time.perf_counter()
greedy_time = t1 - t0
greedy_cost = calculate_total_distance(greedy_routes, data)

print(f"\n1. Greedy Construction Solution:")
print(f"   Routes: {greedy_routes}")
print(f"   Total Route Distance Cost: {greedy_cost:.2f}")
print(f"   Execution Time: {greedy_time:.6f} seconds")

# Run Local Search Optimization Refinement
t0 = time.perf_counter()
optimized_routes = local_search_swap(greedy_routes, data, capacity)
t1 = time.perf_counter()
local_time = t1 - t0
optimized_cost = calculate_total_distance(optimized_routes, data)

print(f"\n2. Local Search Optimized (Swap Move) Solution:")
print(f"   Routes: {optimized_routes}")
print(f"   Total Route Distance Cost: {optimized_cost:.2f}")
print(f"   Execution Time: {local_time:.6f} seconds")