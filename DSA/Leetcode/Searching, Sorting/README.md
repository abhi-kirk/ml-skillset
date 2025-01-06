# Binary Search
*Definition*: 
- Searching for an element or index in an ordered array. 
- Divides the search space in 2 after every comparison. 

*What makes binary search work is that there exists a function that can map elements in left half to True, and the other half to False, or vice versa. If we can find such a function, we can apply binary search to find the boundary (lower_bound for example).*
  
## Templates
### Generalized Binary Search
Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:

**Minimize `k` , s.t. `condition(k)` is True**
```py
def binary_search(array):

    left, right = min(search_space), max(search_space)

    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left
```
The return value is the minimal `k`​ satisfying the `condition(k)` function. The value can be `left` or `left - 1`. 

*If we can discover some kind of monotonicity, for example, if `condition(k)` is True then `condition(k+1)` is True, then we can consider binary search.*