# Data Search

**Summary**

## Data Search

Data search is a crucial aspect of computer science, as it allows us to efficiently find specific pieces of information within a dataset. This process is essential in various applications, including database management, information retrieval, and data analysis.

### O() Notation

When analyzing the performance of searching algorithms, computer scientists use O() notation to describe the time complexity of the algorithm. O() notation provides a rough approximation of how the algorithm's execution time grows as the input size increases.

- **O(1)**: Constant time, independent of input size. This is the ideal scenario, as the algorithm's performance remains consistent regardless of the input size.
- **O(log N)**: Logarithmic time, grows slowly with input size. Algorithms with logarithmic time complexity are highly efficient, as the execution time increases only logarithmically with the input size.
- **O(N)**: Linear time, often the baseline. Algorithms with linear time complexity are efficient for small input sizes but become less efficient as the input size grows.
- **O(Nk)**: Polynomial time, quadratic, cubic, etc. Algorithms with polynomial time complexity are not as efficient as those with logarithmic or linear time complexity, and their execution time can become significant for large input sizes.
- **O(kN)**: Exponential time, very bad. Algorithms with exponential time complexity are highly inefficient and are typically not practical even for reasonably small input sizes.

### Searching for an Element in Memory

**Unsorted Data in a Linked List**

- Start from the beginning.
- Proceed stepwise, comparing each element.
- Stop if found and return the element's location.
- If the end of the list is reached, return not found.
- **Time Complexity**: O(N), where N is the number of elements in the list.

**Unsorted Data in an Array**

- Start from the beginning.
- Proceed stepwise, comparing each element.
- Stop if found and return the element's location.
- If the end of the array is reached, return not found.
- **Time Complexity**: O(N), where N is the number of elements in the array.

**Sorted Data in an Array**

- Start from the beginning.
- Proceed stepwise, comparing each element.
- Stop if found and return the element's location.
- If the end of the array is reached, return not found.
- **Time Complexity**: O(N), but...

**Binary Search (Sorted Data in an Array)**

- Look at the middle element in the array:
  - If it is greater than the target, search in the lower half.
  - If it is less than the target, search in the upper half.
- Switch focus to the new array, which is half the size of the original.
- Repeat.
- **Time Complexity**: O(log N), where N is the number of elements in the array.

### Problems with Arrays

- **Fixed Size**: The size of an array must be fixed ahead of time.
- **Adding Entries**: Adding new entries requires resizing the array, which can be inefficient for large arrays.
- **Maintaining Sorted Order**: Maintaining sorted order in an array is O(N), as it requires finding the location to insert, moving all further elements by 1 to create a gap, and inserting the new element.
- **Deleting Entries**: Deleting entries also requires O(N) time, as it involves finding the location, deleting the element, and moving all subsequent entries down by 1 step.

### Alternatives to Arrays

**Binary Search Tree (BST)**

- **Advantages**:
  - Easier to maintain sorted order as the tree grows.
- **Disadvantages**:
  - BSTs can become unbalanced, resulting in O(N) time complexity.

**Self-Balancing BSTs**

- **Advantages**:
  - Address the unbalancing issue in BSTs.
  - Maintain reasonable time complexity even for large datasets.
- **Examples**: Red-black trees, AVL trees, B-trees

**Hash Tables**

- **Advantages**:
  - O(1) time complexity for computing an index for an element.
- **Disadvantages**:
  - Relies on the assumption that the index for each element is unique, which can be difficult to guarantee.
