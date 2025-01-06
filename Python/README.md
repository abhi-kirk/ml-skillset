## Python

### Misc.
- Check if `float` is integer: `f.is_integer()`
- Check datatype: `isinstance(val, dType)`
---

### Array Sorting
Sort array `A`, in descending order, by a particular column with index `i`:
- New array: `sorted(A, key=lambda x: x[i], reverse=True)`
  - Remove `reverse` for ascending order. 
- In-Place: `A.sort(key=lambda x: -x[i])`
  - Remove `-` for ascending order. 
- Time Complexity: $O(n\log n)$
---

### Create Matrices
Create zero matrix of pre-specified size $m*n$:
- `grid = [[0] * n] * m`
  ---