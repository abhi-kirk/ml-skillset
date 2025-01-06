## Min-Heap (Priority Queue)
**Theory**:
- Heaps are binary trees where each parent node has a value less than or equal to the any of its children. 
- The smallest element is always the root. 
- Python `heapq`:
  - Uses zero-based indexing, 
  - `pop` method always returns the smallest element. 

**[Methods](https://docs.python.org/3/library/heapq.html)**
- `heapq.heapify(x)`: Transform list `x` into a heap, in-place: $O(n)$. 
- `heapq.heappush(heap, item)`: Push `item` onto the heap: $O(\log n)$. 
- `heapq.heappop(heap)`: Pop and return the smallest item from heap: $O(\log n)$. 
- `heapq.heappushpop(heap, item)`
- `heapq.heapreplace(heap, item)`