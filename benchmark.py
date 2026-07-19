import time
import matplotlib.pyplot as plt
from load_cities import get_subset
from bst import BST  # Assumes your BST class has insert(root, key, val) and search(root, key)
from avl import AVLTree
from heap import MinHeap
from hashtable import HashTable

def run_benchmarks():
    sizes = [100, 1000, 10000]
    
    # Data tracking for plotting
    results = {
        'BST': {'insert': [], 'search': []},
        'AVL': {'insert': [], 'search': []},
        'Min-Heap': {'insert': [], 'search': []},
        'Hash Table': {'insert': [], 'search': []}
    }

    print(f"{'Structure':<15} | {'N':<6} | {'Insert Time (s)':<15} | {'Search Time (s)':<15}")
    print("-" * 60)

    for n in sizes:
        # Load random subset for this run
        cities = get_subset(n, 'random')
        target_id = cities[-1].id  # Target the last inserted city for search test
        target_dist = cities[-1].distance

        # --- 1. BST Benchmark ---
        bst_tree = BST()
        bst_root = None
        
        t0 = time.perf_counter()
        for c in cities:
            # If your BST automatically updates its internal root:
            bst_tree.insert(c.id, c) 
        t1 = time.perf_counter()
        bst_insert_time = t1 - t0
        
        t0 = time.perf_counter()
        bst_tree.search(target_id)
        t1 = time.perf_counter()
        bst_search_time = t1 - t0
        
        results['BST']['insert'].append(bst_insert_time)
        results['BST']['search'].append(bst_search_time)
        print(f"{'BST':<15} | {n:<6} | {bst_insert_time:<15.6f} | {bst_search_time:<15.6f}")

        # --- 2. AVL Benchmark ---
        avl_tree = AVLTree()
        avl_root = None
        
        t0 = time.perf_counter()
        for c in cities:
            avl_root = avl_tree.insert(avl_root, c.id, c)
        t1 = time.perf_counter()
        avl_insert_time = t1 - t0
        
        t0 = time.perf_counter()
        avl_tree.search(avl_root, target_id)
        t1 = time.perf_counter()
        avl_search_time = t1 - t0
        
        results['AVL']['insert'].append(avl_insert_time)
        results['AVL']['search'].append(avl_search_time)
        print(f"{'AVL':<15} | {n:<6} | {avl_insert_time:<15.6f} | {avl_search_time:<15.6f}")

        # --- 3. Min-Heap Benchmark ---
        heap = MinHeap()
        
        t0 = time.perf_counter()
        for c in cities:
            heap.insert(c)
        t1 = time.perf_counter()
        heap_insert_time = t1 - t0
        
        # Min-heap searches by popping out until finding the item or peaking
        t0 = time.perf_counter()
        heap.peek_min()  # Standard heap priority access operation
        t1 = time.perf_counter()
        heap_search_time = t1 - t0
        
        results['Min-Heap']['insert'].append(heap_insert_time)
        results['Min-Heap']['search'].append(heap_search_time)
        print(f"{'Min-Heap':<15} | {n:<6} | {heap_insert_time:<15.6f} | {heap_search_time:<15.6f}")

        # --- 4. Hash Table Benchmark ---
        ht = HashTable(capacity=n*2)
        
        t0 = time.perf_counter()
        for c in cities:
            ht.insert(c.id, c)
        t1 = time.perf_counter()
        ht_insert_time = t1 - t0
        
        t0 = time.perf_counter()
        ht.search(target_id)
        t1 = time.perf_counter()
        ht_search_time = t1 - t0
        
        results['Hash Table']['insert'].append(ht_insert_time)
        results['Hash Table']['search'].append(ht_search_time)
        print(f"{'Hash Table':<15} | {n:<6} | {ht_insert_time:<15.6f} | {ht_search_time:<15.6f}")
        print("-" * 60)

    # --- Plotting the Graphs ---
    plt.figure(figsize=(12, 5))

    # Insertion Plot
    plt.subplot(1, 2, 1)
    for struct in results:
        plt.plot(sizes, results[struct]['insert'], marker='o', label=struct)
    plt.title('Insertion Runtime Comparison')
    plt.xlabel('Dataset Size (N)')
    plt.ylabel('Time (Seconds)')
    plt.grid(True)
    plt.legend()

    # Search/Access Plot
    plt.subplot(1, 2, 2)
    for struct in results:
        plt.plot(sizes, results[struct]['search'], marker='o', label=struct)
    plt.title('Search/Access Runtime Comparison')
    plt.xlabel('Dataset Size (N)')
    plt.ylabel('Time (Seconds)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig('performance_chart.png')
    print("\nBenchmark complete! Graph saved as 'performance_chart.png'.")

if __name__ == "__main__":
    run_benchmarks()