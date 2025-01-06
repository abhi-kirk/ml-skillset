**Usage**
- Linked lists implements *Queues*, *Stacks* and *Graphs*:
  - Queues are FIFO, 
  - Stacks are LIFO, 
  - Graphs are hash tables with:
    - Keys as graph nodes,
    - Values as linked lists, where linked list values are nodes connected to the key node. These represent vertices from the key node. 
    - Called Adjacency list. 
    - This DS is similar to how Graph DBs store data. 
---

**Performance**
- In Python, linked lists are dynamic arrays - hence memory usage of both lists and linked lists is very similar. 
- *Time Complexity*:
  - Insertion/Deletion:
    - List Insert: `.insert()` (specific position) or `.append()` (end of list). Complexity: $O(n)$. 
    - List Delete: `.remove()` (specific position) or `.pop()` (end of list). Complexity: $O(n)$. 
    - Linked Lists complexity for insertion/deletion is always $O(1)$.
  - Retrieval:
    - List Retrieval complexity: $O(1)$. 
    - Linked List Retrieval complexity: $O(n)$. 
  - Searching:
    - For both cases complexity is $O(n)$. 
---

**Double-Ended Queue**
- `collections.deque` module provides an implementation of linked lists to access, insert or remove elements in $O(1)$. 
  - Double-ended: Can implement both Stacks and Queues. 
---
