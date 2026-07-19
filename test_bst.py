import sys
sys.path.insert(0, '../datasets')
from load_cities import get_subset
from bst import BST

cities = get_subset(10, 'random')
tree = BST()

for c in cities:
    tree.insert(c['id'], c)

print('Inserted', len(cities), 'cities')
print('In-order keys:', tree.in_order())
print('Tree height:', tree.height())

test_city = cities[3]
found = tree.search(test_city['id'])
print('Search for', test_city['id'], '->', found['name'] if found else 'NOT FOUND')

tree.delete(test_city['id'])
print('After delete, search again ->', tree.search(test_city['id']))