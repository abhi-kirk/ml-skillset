**Properties**
- Objectives:
  - Find the min or max of something, 
  - Make decisions that might look different depending on the decisions made previously. 
- Approaches:
  - Top-down: Recursion + Memoization
  - Bottom-up: Tabulation

---

**Bottom-up (Tabulation)**
- Done iteratively, and is based on the concept of *overlapping subproblems* and *optimal substructure*. 
- The problem can be constructed from solutions to similar and smaller subproblems. 
- Example: Cost to solve a problem in $n$ steps := Cost to solve a problem in $(n-1)$ steps + Cost of the $n^{th}$ step. 

---

**Top-Down (Recursion + Memoization)**
- We start at the top (beginning) and work our way to the base cases. 
- Implemented with Recursion, and made efficient using memoization. 
  - Recursion is used to solve the smaller sub-problems, starting from the full problem. However this can lead to an exponential growth of the call stack because of repeated recursion calls to calculate the same cost. 
  - Memoization refers to storing the cost values in a hash map. A function can also be memoized using the `@cache` decorator on top (part of the `functools` module in Python3). 