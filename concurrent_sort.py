import time
import threading
from load_cities import get_subset

# Thread management globals
active_threads_count = 0
thread_counter_lock = threading.Lock()  # Mutex Lock for Thread Safety

def sequential_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sequential_merge_sort(arr[:mid])
    right = sequential_merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].id <= right[j].id:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Concurrent Multi-Threaded Sorting System ---
def concurrent_merge_sort(arr, max_threads):
    global active_threads_count
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    
    # Check if we can safely spawn new threads within limits
    spawn_thread = False
    with thread_counter_lock:  # CRITICAL SECTION Protected by Mutex Lock
        if active_threads_count < max_threads:
            active_threads_count += 1
            spawn_thread = True

    if spawn_thread:
        left_container = []
        # Spawn worker thread to handle the left half of the array partition
        t = threading.Thread(target=lambda: left_container.extend(concurrent_merge_sort(arr[:mid], max_threads)))
        t.start()
        
        # Main thread concurrently processes the right half partition
        right = concurrent_merge_sort(arr[mid:], max_threads)
        t.join()  # Thread Synchronization Barrier
        
        with thread_counter_lock:  # CRITICAL SECTION: Safe decrement
            active_threads_count -= 1
            
        left = left_container
    else:
        # Fall back to standard sequential execution if thread allocation limits are maxed out
        left = sequential_merge_sort(arr[:mid])
        right = sequential_merge_sort(arr[mid:])
        
    return merge(left, right)

def benchmark_concurrency():
    print("=== Task 5 Concurrency Benchmark Run ===")
    dataset_size = 10000
    cities_data = get_subset(dataset_size, 'random')
    
    # 1. Measure Baseline Sequential Performance
    t0 = time.perf_counter()
    sequential_merge_sort(cities_data.copy())
    t_sequential = time.perf_counter() - t0
    print(f"Sequential Baseline (1 Thread equivalent): {t_sequential:.4f} seconds")
    print("-" * 55)
    print(f"{'Thread Count':<15} | {'Execution Time (s)':<20} | {'Speedup Factor':<15}")
    print("-" * 55)
    print(f"{'1 Thread (Seq)':<15} | {t_sequential:<20.4f} | {'1.00x':<15}")

    # 2. Benchmark Thread Scalability across 2, 4, and 8 Threads
    for threads in [2, 4, 8]:
        global active_threads_count
        active_threads_count = 1 # Reset thread counter state
        
        t0 = time.perf_counter()
        concurrent_merge_sort(cities_data.copy(), max_threads=threads)
        t_concurrent = time.perf_counter() - t0
        
        speedup = t_sequential / t_concurrent
        print(f"{threads:<15} | {t_concurrent:<20.4f} | {speedup:.2f}x")
    print("-" * 55)

if __name__ == "__main__":
    benchmark_concurrency()