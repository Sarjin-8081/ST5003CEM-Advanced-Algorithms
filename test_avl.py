from load_cities import get_subset
from avl import AVLTree

# Load 10 sorted cities to prove AVL handles worst-case data flawlessly
cities = get_subset(10, 'sorted')

tree = AVLTree()
root = None

for city in cities:
    root = tree.insert(root, city.id, city)

print(f"Inserted {len(cities)} cities successfully into AVL.")
print(f"Balanced AVL Tree Height: {tree.get_height(root)}")

# Test Search
search_target = cities[4].id
result = tree.search(root, search_target)
if result:
    print(f"Search successful! Found: {result.value}")