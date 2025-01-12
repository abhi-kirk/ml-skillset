# Basic Language Models

## Bigram
- *Definition*: Bigram is simply building a frequency dictionary, where the key is two contiguous letters taken at a time from a string. 
  - This gives us a bigram matrix, where the rows and columns are unique letters. 
  - For each row in this matrix, we hence have a probability distribution (dividing the counts by the row sum) which we can sample from. 
- *Language model*: Start from a character, and keep sampling for the next character using the bigram matrix, until you reach the special character denoting end of string. 


## Negative log-likelihood
