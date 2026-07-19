from load_cities import get_subset
from heap import MinHeap

# Grab 10 random cities
cities = get_subset(10, 'random')

pq = MinHeap()
for city in cities:
    pq.insert(city)

print(f"Inserted {pq.size()} cities into the Priority Queue (Min-Heap).")
print(f"Top element (should be closest): {pq.peek_min()}\n")

print("Extracting cities in order of distance:")
while pq.size() > 0:
    closest = pq.extract_min()
    print(f" -> {closest.name} | Distance: {closest.distance:.2f}")