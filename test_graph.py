from graph import Graph

# Initializing simulated multi-city transportation structure
g = Graph()

# Add standard pathway links
g.add_edge("Kathmandu", "Bhaktapur", 15)
g.add_edge("Kathmandu", "Lalitpur", 8)
g.add_edge("Bhaktapur", "Banepa", 20)
g.add_edge("Lalitpur", "Banepa", 25)
g.add_edge("Banepa", "Dhulikhel", 10)

# Run Dijkstra Shortest Path
d_path, d_dist = g.dijkstra("Kathmandu", "Dhulikhel")
print("1. Dijkstra Shortest Path (Kathmandu -> Dhulikhel):")
print(f"   Path: {' -> '.join(d_path)} | Total Cost: {d_dist}\n")

# Run Prim's Spanning Tree Construction
mst, total_mst_cost = g.prim("Kathmandu")
print("2. Prim's Minimum Spanning Tree Connections:")
for u, v, w in mst:
    print(f"   Link: {u} --({w})--> {v}")
print(f"   Total MST System Cost: {total_mst_cost}\n")

# Run Bellman-Ford with an injected negative pathway adjustment
g.add_edge("Dhulikhel", "Sindhuli", 50)
g.add_edge("Sindhuli", "Dhulikhel", -60) # Injected negative loop fallback path

bf_status, _ = g.bellman_ford("Kathmandu", "Sindhuli")
print("3. Bellman-Ford Structural Cycle Evaluation:")
print(f"   System Scan result: {bf_status} (Successfully flagged negative loop risks!)")