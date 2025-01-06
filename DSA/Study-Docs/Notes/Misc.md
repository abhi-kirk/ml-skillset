***Logarithms***: 
- $log_{10} 100$ is like asking: **How many 10s do we multiply together to get 100?** 

---

**Binary Search Tree (BST)**:
- Tree implementation of *Binary Search* algorithm. 
- The left child is always smaller than the root, and the right child is always larger. 
- <img src="imgs/Screenshot 2022-11-28 at 7.04.18 AM.png" width=400>
- Complexity: $O(log\space n)$ for searching, inserting and deleting. 
- <img src="imgs/Screenshot 2022-11-28 at 7.06.14 AM.png" width=400>
- No random access, i.e. cannot ask for "5th element of this tree". 
- Performance times rely on the Tree being *Balanced*. 
	- Example of tree (special type of BST) that balances itself: [*Red-Black Tree*](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) 
		- Each node stores and extra bit represeting "color" used to ensure that the tree remains balanced during insertions and deletions. 
		- [*B-Trees*](https://en.wikipedia.org/wiki/B-tree) (special type of BST) are commonly used to store data in DBs. 
			- Also self-balancing. 
			- Generalization of BST; allows for nodes with more than two children. 

---

**Inverted Index**
- Hash map which stores a mapping from content, e.g.
	- From words/numbers to their locations in a table/document(s). 
- Allows fast full-text searches at a cost of increased processing when a document is added to the DB. 
- Central component in search engines algorithms. 


---

**Parallel Algorithms**
- The best we can do with a sorting algorithm is $O(nlog\space n)$
	- Cannot sort in $O(n)$ unless we use parallel algorithm. E.g. Parallel Quicksort will give $O(n)$. 
- Time gains are not linear because of:
	- Overhead of managing parallelism, 
	- Load balancing. 

---

**MapReduce**
- Distributed algorithm; can be used through *Apache Hadoop*. 
- *Map*:
	- Takes an array and applies the same function to each element of the array. 
	- Example: `[1,2,3,4] -> lambda --> [2,4,6,8]`
	- Parallelizing assuming independence. 
- *Reduce*:
	- Transform an array to a single item. 
	- Example: `[1,2,3,4] -> sum -> 15`

---

**Bloom Filters & HyperLogLog**
- *Bloom Filters*:
	- Space-efficient probabilistic data structures. 
	- Function is to check if an element is a member of a set. 
		- Hash tables can be used with $O(1)$ but if the dataset is huge, storage will be a concern since all keys need to be stored. 
		- Bloom filters don't need to store all keys. 
	- False Positives are possible, but False Negatives are not. 
		- I.E. a query returns either "possible in set" or "definitely not in set". 
	- Bloom Filters are great when we don;t need an exact answer. 
	- Uses:
		- Fruit flies: To detect novelty of odors, 
		- Google Chrome: (past) To identify malicious URLs, 
		- Medium: To avoid recommending articles a user has previously read. 
- *HyperLogLog*:
	- Approximates the number of unique elements in a set, and only using a fraction of the memory a task like this would otherwise take. 
	- Uses:
		- Amazon: Get a list of unique items that all users have viewed in a day. 
		- Google: Get a list of unique webpages that all users have accessed in a day. 

---
