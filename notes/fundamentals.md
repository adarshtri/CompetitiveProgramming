# Fundamentals for Technical Interviews

## 🧮 Time & Space Complexity

### Big O Notation
- **O(1)**: Constant time - operations that don't depend on input size
- **O(log n)**: Logarithmic - binary search, divide and conquer
- **O(n)**: Linear - single loop through data
- **O(n log n)**: Linearithmic - sorting algorithms, divide and conquer
- **O(n²)**: Quadratic - nested loops
- **O(2ⁿ)**: Exponential - recursive algorithms without memoization
- **O(n!)**: Factorial - permutations, traveling salesman

### Common Complexities
```python
# O(1) - Constant
def get_first_element(arr):
    return arr[0]

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

## 📊 Data Structures Overview

### 1. Arrays & Strings
- **Access**: O(1)
- **Search**: O(n)
- **Insert/Delete**: O(n) (shifting required)
- **Key Techniques**: Two pointers, sliding window, prefix sums

### 2. Linked Lists
- **Access**: O(n)
- **Search**: O(n)
- **Insert/Delete**: O(1) (if you have the node)
- **Key Techniques**: Fast/slow pointers, reversal, dummy nodes

### 3. Trees
- **Height-balanced**: O(log n) for search/insert/delete
- **Unbalanced**: O(n) worst case
- **Key Techniques**: DFS, BFS, recursion, iterative traversal

### 4. Graphs
- **Adjacency List**: O(V + E) space, O(degree) for neighbors
- **Adjacency Matrix**: O(V²) space, O(1) for edge check
- **Key Techniques**: DFS, BFS, topological sort, shortest path

### 5. Hash Tables
- **Average**: O(1) for all operations
- **Worst**: O(n) due to collisions
- **Key Uses**: Frequency counting, deduplication, caching

## 🔄 Common Algorithm Patterns

### 1. Two Pointers
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

### 2. Sliding Window
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 3. Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

## 🎯 Problem-Solving Framework

### 1. Understand the Problem
- Read carefully, identify inputs/outputs
- Ask clarifying questions
- Consider edge cases

### 2. Plan Your Approach
- Think of brute force first
- Identify patterns or data structures
- Consider time/space trade-offs

### 3. Implement
- Write clean, readable code
- Use meaningful variable names
- Add comments for complex logic

### 4. Test & Optimize
- Test with examples
- Check edge cases
- Look for optimization opportunities

## 💡 Key Interview Tips

1. **Clarify Requirements**: Don't assume, ask questions
2. **Start Simple**: Begin with brute force, then optimize
3. **Think Aloud**: Explain your thought process
4. **Consider Trade-offs**: Time vs space complexity
5. **Test Your Code**: Walk through examples
6. **Handle Edge Cases**: Empty inputs, single elements, etc.

## 📝 Common Mistakes to Avoid

- Not considering edge cases
- Ignoring time/space complexity
- Not testing with examples
- Rushing to code without planning
- Forgetting to handle null/empty inputs
- Not explaining your approach clearly 