## Set
Use sets when hash map speedup is not needed, but uniqueness is. 
- Properties:
  - Sets are unordered and mutable. 
- Initialize: `a = set()`
- Append elements (in-place): `a.add(elem)`
- Remove element (in-place): `a.remove(elem)`
- Remove all elements (in-place): `a.clear()`
- Shallow copy: `b = a.copy()`
  - An `=` operator to `a` or `b` will modify both sets. 
  - Modification with above-mentioned methods will not. 
- Difference:
  - `a-b`
  - In-place: `a.difference_update(b)`
- Intersection: `c = a.intersection(b)` or `c = a & b`


## Queue
Double-ended Queue data structure:
- `from collections import deque`
- Create from list: `queue = deque(listObj)`
- Appending elements: 
  - At the end end: `queue.append(elem)`
  - At the left end: `queue.appendleft(elem)`
- Popping elements:
  - From the right end: `queue.pop()`
  - From the left end: `queue.popleft()`
- Accessing elements:
  - Return first index of the element starting searching from `beg` till `end` index: `queue.index(elem, beg, end)`. 
  - Insert element at the specified index: `queue.insert(index, elem)`. 
  - Removes the first occurrence of the element: `queue.remove(elem)`. 
  - Count the number of occurrences of the element: `queue.count(elem)`. 


## Heap
Heaps are binary trees for which every parent node has a value less than or equal to the children. Also called *priority queues*. Python implementation is a *min-heap*, i.e. maintains ascending order in the heap. 
- `import heapq`
- Create from list, in-place, $O(n)$: `heapq.heapify(listObj)` 
- Appending elements, $O(\log n)$: `heapq.heappush(heap, elem)`
- Popping elements, $O(\log n)$; always returns the smallest: `heapq.heappop(heap)`
- Accessing smallest element: `heap[0]`
  - This is for accessing the smallest only - rest of the (sorted) heap can only be accessed using `heappop()`. 
- For consecutive inserts and removals:
  - Using consecutive calls to `heappush, heappop`: $O(n\log n)$. 
  - Creating a list and then using `heapify`: $O(n)$. 
- Tuples (`int`, `str`), or a list of tuples, can be used in a heap. 


## Hash Map
- `hash()` is a deterministic function which can generate hash values (fixed-size outputs) for *almost* any Python object. However, for strings, a random initialization is used in Python to make the hash value less predictable (to, in turn, safeguard against DoD attacks). 
  - Random initialization can be disabled manually by setting a seed. 
  - Not all objects have a corresponding hash value, e.g. lists, sets, dicts (built-in mutable types). 