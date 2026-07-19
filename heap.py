"""
Min-Heap (Priority Queue) - Task 1, ST5003CEM
Array-based, ordered by 'distance' -- supports fetching the nearest
unvisited city in O(log n), and peeking the nearest in O(1).
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, city):
        self.heap.append(city)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i]["distance"] < self.heap[parent]["distance"]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self.heap)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < n and self.heap[left]["distance"] < self.heap[smallest]["distance"]:
                smallest = left
            if right < n and self.heap[right]["distance"] < self.heap[smallest]["distance"]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest