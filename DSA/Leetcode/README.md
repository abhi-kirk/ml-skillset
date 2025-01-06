# Notes

## Python In-Built Methods Time Complexities
- `int` <--> `str`: $O(n)$
- `sort`: $O(n\log n)$
  - Timesort algorithm
- `list` <--> `set`: $O(n)$
- `append`, `pop`: $O(1)$
- `min`, `max`: $O(n)$


## Useful Just-In-Case
$$\text{ceil}(\frac{a}{b}) = \frac{a-1}{b} + 1$$


## During the Interview
- After completing the solution: 
  - Add various conditions (even if redundant) to check for edge cases based on problem constraints. 
  - Write down the time and space complexities on top of the method as comments. 
- Create your own test cases and run them before submitting the solution. 


## Remember
- Modifying an input data structure in-memory will:
  - Almost always lead to better space complexity
  - But is never recommended as a general software practice since the original value might be needed in other parts of the code. 