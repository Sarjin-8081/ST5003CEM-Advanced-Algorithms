import matplotlib.pyplot as plt
import networkx as nx

# Define the multi-city transportation network graph nodes and directional routes
edges = [
    ("Kathmandu", "Bhaktapur", 15),
    ("Kathmandu", "Lalitpur", 8),
    ("Bhaktapur", "Banepa", 20),
    ("Lalitpur", "Banepa", 25),
    ("Banepa", "Dhulikhel", 10)
]

# Set fixed programmatic coordinates to replicate a real geographic distribution layout
pos = {
    "Kathmandu": (0, 1),
    "Lalitpur": (1, 0),
    "Bhaktapur": (2, 2),
    "Banepa": (4, 1),
    "Dhulikhel": (6, 1)
}

def draw_dijkstra():
    G = nx.DiGraph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        
    plt.figure(figsize=(8, 5))
    plt.title("Task 2: Dijkstra's Shortest Path Optimization\n(Kathmandu -> Lalitpur -> Banepa -> Dhulikhel | Total Cost: 43)", fontsize=11, fontweight='bold')
    
    # Define color scheme masks to highlight the shortest path tree sequence links
    dijkstra_edges = [("Kathmandu", "Lalitpur"), ("Lalitpur", "Banepa"), ("Banepa", "Dhulikhel")]
    edge_colors = ['#2ca02c' if (u, v) in dijkstra_edges else '#a0a0a0' for u, v in G.edges()]
    edge_widths = [4.5 if (u, v) in dijkstra_edges else 1.5 for u, v in G.edges()]
    
    nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='#1f77b4')
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', font_color='white')
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, arrowsize=18, min_source_margin=15, min_target_margin=15)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, font_weight='bold', label_pos=0.5)
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('dijkstra_shortest_path.png', dpi=300)
    plt.close()

def draw_prim():
    # Prim's algorithm evaluates global minimal connectivity connections
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
        
    plt.figure(figsize=(8, 5))
    plt.title("Task 2: Prim's Minimum Spanning Tree Construction\n(Total Optimal Infrastructure System Footprint Cost: 53)", fontsize=11, fontweight='bold')
    
    mst_edges = [("Kathmandu", "Lalitpur"), ("Kathmandu", "Bhaktapur"), ("Bhaktapur", "Banepa"), ("Banepa", "Dhulikhel")]
    edge_colors = ['#17becf' if G.has_edge(u, v) and ((u, v) in mst_edges or (v, u) in mst_edges) else '#e0e0e0' for u, v in G.edges()]
    edge_styles = ['solid' if G.has_edge(u, v) and ((u, v) in mst_edges or (v, u) in mst_edges) else 'dashed' for u, v in G.edges()]
    edge_widths = [4.5 if G.has_edge(u, v) and ((u, v) in mst_edges or (v, u) in mst_edges) else 1.0 for u, v in G.edges()]
    
    nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='#7f7f7f')
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', font_color='white')
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, style=edge_styles, width=edge_widths)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, font_weight='bold')
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('prim_mst.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    draw_dijkstra()
    draw_prim()
    print("Success! Both 'dijkstra_shortest_path.png' and 'prim_mst.png' have been successfully generated in your directory.")