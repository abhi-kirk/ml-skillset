## [Python Time Complexity Chart](https://wiki.python.org/moin/TimeComplexity)

## 2's Complement
- The computer stores negatives integers with 2's complement binary representation:
  - Flip bits, then 
  - Add 1. 
- Signed integers are identified by the compiler by checking overflow during mathematical operations. 
  - The hardware does not care about signed/unsigned representation. 
- When flipping bits, don't ignore the leading zeros in the binary representation. 