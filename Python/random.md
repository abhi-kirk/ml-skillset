# `np.random`

## General
- Logarithm: `np.log2()`

---

## Array Randomization

### Generate random arrays with `np.random.randint(), np.random.rand()`:
- Integers: 
  - Single int between 0 and k: `np.random.randint(k)`
  - Int array of size n, elements between 0 and k: `np.random.randint(k, size=(n))`
    - n can be a tuple to generate matrices
- Floats:
  - Single float between 0 and 1: `np.random.rand()`
  - Float array of size n: `np.random.rand(n)`
    - n can be a tuple to generate matrices

### Choose from a given array with `np.random.choice()`:
- One of the values: `np.random.choice(arr)`
- Create array of size n: `np.random.choice(arr, size=n)`
  - n can be a tuple to generate matrices

---

## Data Distribution