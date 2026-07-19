"""
Hash Table (Chaining) - Task 1, ST5003CEM
Fixed-size array of buckets; collisions resolved with chaining.
O(1) average insert/search/delete; O(n) worst case if all keys collide.
"""


class HashTable:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        bucket = self.table[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def search(self, key):
        for k, v in self.table[self._index(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        bucket = self.table[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False