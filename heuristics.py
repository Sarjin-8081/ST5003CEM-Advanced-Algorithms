import time
import math

# Problem definition setup
class Customer:
    def __init__(self, cust_id, x, y, demand, ready_time, due_time):
        self.id = cust_id
        self.x = x
        self.y = y
        self.demand = demand
        self.ready_time = ready_time
        self.due_time = due_time

def calculate_distance(c1, c2):
    return math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)

# Calculate total route system distance cost
def calculate_total_distance(routes, customers):
    depot = customers[0]
    total_dist = 0
    for route in routes:
        if not route:
            continue
        # Distance from depot to first customer
        total_dist += calculate_distance(depot, customers[route[0]])
        # Distance between customers
        for i in range(len(route) - 1):
            total_dist += calculate_distance(customers[route[i]], customers[route[i+1]])
        # Distance from last customer back to depot
        total_dist += calculate_distance(customers[route[-1]], depot)
    return total_dist

# --- Heuristic 1: Greedy Construction Heuristic ---
def greedy_vrptw(customers, vehicle_capacity):
    depot = customers[0]
    unvisited = set(range(1, len(customers)))
    routes = []
    
    while unvisited:
        curr_route = []
        curr_load = 0
        curr_time = 0
        curr_node = depot
        
        while unvisited:
            best_next = None
            best_dist = float('inf')
            
            for c_id in unvisited:
                c = customers[c_id]
                dist = calculate_distance(curr_node, c)
                arrival_time = curr_time + dist
                
                # Check Capacity and Time Window constraints
                if curr_load + c.demand <= vehicle_capacity and arrival_time <= c.due_time:
                    if dist < best_dist:
                        best_dist = dist
                        best_next = c_id
            
            if best_next is not None:
                c = customers[best_next]
                curr_route.append(best_next)
                curr_load += c.demand
                # Wait if arriving before the customer is ready
                curr_time = max(c.ready_time, curr_time + best_dist)
                curr_node = c
                unvisited.remove(best_next)
            else:
                # No more customers can fit this vehicle; return to depot
                break
        routes.append(curr_route)
    return routes

# --- Heuristic 2: Local Search (Node Swap Move Optimization) ---
def local_search_swap(routes, customers, vehicle_capacity):
    optimized_routes = [r[:] for r in routes]
    improved = True
    
    while improved:
        improved = False
        # Try swapping nodes between distinct positions
        for r1 in range(len(optimized_routes)):
            for r2 in range(len(optimized_routes)):
                for i in range(len(optimized_routes[r1])):
                    for j in range(len(optimized_routes[r2])):
                        if r1 == r2 and i >= j:
                            continue
                            
                        # Perform temporary swap
                        optimized_routes[r1][i], optimized_routes[r2][j] = optimized_routes[r2][j], optimized_routes[r1][i]
                        
                        # Validate if both routes remain structurally feasible
                        if validate_route(optimized_routes[r1], customers, vehicle_capacity) and \
                           validate_route(optimized_routes[r2], customers, vehicle_capacity):
                            
                            old_dist = calculate_total_distance(routes, customers)
                            new_dist = calculate_total_distance(optimized_routes, customers)
                            
                            if new_dist < old_dist:
                                routes = [r[:] for r in optimized_routes]
                                improved = True
                                break
                        # Undo swap if constraints violated or no cost improvement
                        optimized_routes[r1][i], optimized_routes[r2][j] = optimized_routes[r2][j], optimized_routes[r1][i]
                    if improved: break
                if improved: break
            if improved: break
    return routes

def validate_route(route, customers, capacity):
    depot = customers[0]
    curr_load = 0
    curr_time = 0
    curr_node = depot
    
    for c_id in route:
        c = customers[c_id]
        curr_load += c.demand
        if curr_load > capacity:
            return False
        dist = calculate_distance(curr_node, c)
        curr_time = max(c.ready_time, curr_time + dist)
        if curr_time > c.due_time:
            return False
        curr_node = c
    return True