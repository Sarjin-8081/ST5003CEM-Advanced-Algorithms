from load_cities import get_subset
from hashtable import HashTable

# Load 10 random cities
cities = get_subset(10, 'random')

ht = HashTable(capacity=20)  # Small capacity to test chaining structure
for city in cities:
    ht.insert(city.id, city)

print(f"Inserted {ht.size} cities into the Hash Table.")

# Test Search
target_id = cities[2].id
found_city = ht.search(target_id)
print(f"Search for ID {target_id} -> Found: {found_city}")

# Test Delete
print(f"Deleting ID {target_id}...")
ht.delete(target_id)
print(f"Search again for ID {target_id} -> Found: {ht.search(target_id)}")