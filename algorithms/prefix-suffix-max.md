# Prefix/Suffix Max Arrays Technique

## Intuition & Mental Framework

Prefix and suffix max (or min) arrays are powerful tools for efficiently answering range queries or solving problems where you need to know the maximum (or minimum) value to the left or right of each element in an array.

Instead of recalculating the max/min for every query or position, you precompute these values in O(n) time, enabling O(1) lookups later.

## Core Mental Model

- **Prefix Max Array:** For each index i, stores the maximum value from the start up to i.
- **Suffix Max Array:** For each index i, stores the maximum value from i to the end.

Think of these as running "scans" from the left and right, recording the best value seen so far.

## When to Use Prefix/Suffix Max Arrays

- When you need to repeatedly query the max/min to the left or right of each element
- When a problem involves "trapping" or "bounding" values between two sides (e.g., water, stock prices)
- When brute force would be O(n²) but precomputation can reduce it to O(n)

## Example: Trapping Rain Water

Given an elevation map, compute how much water can be trapped after raining.

### Approach
1. For each index, the water trapped is determined by the minimum of the tallest bar to the left and right, minus the current height.
2. Precompute:
    - `l_max[i]`: max height to the left of i (including i)
    - `r_max[i]`: max height to the right of i (including i)
3. For each i, water trapped = min(l_max[i], r_max[i]) - height[i]

### Code Template
```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    l_max = [0] * n
    r_max = [0] * n
    l_max[0] = height[0]
    for i in range(1, n):
        l_max[i] = max(l_max[i-1], height[i])
    r_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        r_max[i] = max(r_max[i+1], height[i])
    water = 0
    for i in range(n):
        water += min(l_max[i], r_max[i]) - height[i]
    return water
```

## Other Use Cases
- **Stock Span Problem:** Find the number of consecutive days before today with a lower stock price
- **Range Maximum/Minimum Queries (static):** Precompute for O(1) queries
- **Histogram Largest Rectangle:** Precompute nearest smaller to left/right

## Step-by-Step Mental Framework
1. **Identify** if you need repeated left/right max/min queries
2. **Precompute** prefix and/or suffix arrays
3. **Use** these arrays to answer queries or compute results in a single pass

## Common Pitfalls
- Forgetting to initialize the first/last element correctly
- Off-by-one errors in array indices
- Not handling empty or single-element arrays

## Practice Problems
- Trapping Rain Water (LeetCode 42)
- Stock Span Problem
- Largest Rectangle in Histogram

## Conclusion

Prefix/suffix max arrays are a key precomputation technique that can turn a brute-force O(n²) solution into an efficient O(n) one. Look for problems where you need to know the "best so far" to the left or right of each element! 