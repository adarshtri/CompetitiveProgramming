# Two Pointers Technique

## Intuition & Mental Framework

The two pointers technique is a fundamental algorithmic pattern that uses two pointers to traverse a data structure (usually an array or linked list) in a single pass, often achieving O(n) time complexity instead of O(n²).

## Core Mental Model

Think of two pointers as **two fingers** moving through your data structure, each with a specific purpose:
- **Left Pointer**: Usually starts at the beginning and moves forward
- **Right Pointer**: Usually starts at the end or a specific position and moves based on conditions

## When to Use Two Pointers

### 1. **Sorted Array Problems**
- **Intuition**: When array is sorted, you can eliminate half the search space in each comparison
- **Mental Model**: "If current sum is too small, move left pointer right. If too large, move right pointer left."

### 2. **Palindrome/String Problems**
- **Intuition**: Check from both ends simultaneously
- **Mental Model**: "Start from outside, work your way in"

### 3. **Remove Duplicates**
- **Intuition**: Keep one pointer for writing, one for reading
- **Mental Model**: "Read with one finger, write with another"

### 4. **Linked List Cycle Detection**
- **Intuition**: Fast and slow pointers will meet if there's a cycle
- **Mental Model**: "Tortoise and hare race"

## Common Patterns & Mental Approaches

### Pattern 1: Opposite Ends (Most Common)
```
[1, 2, 3, 4, 5, 6]
 L           R
```

**Mental Process:**
1. Start with L=0, R=len-1
2. Compare elements at L and R
3. Move the pointer that helps achieve your goal
4. Continue until L >= R

**Example**: Two Sum in sorted array
- If arr[L] + arr[R] < target → move L right (need bigger sum)
- If arr[L] + arr[R] > target → move R left (need smaller sum)

### Pattern 2: Same Direction (Sliding Window)
```
[1, 2, 3, 4, 5, 6]
 L  R
```

**Mental Process:**
1. Start with L=0, R=0
2. Expand R until condition is met
3. Contract L until condition is violated
4. Track optimal result during process

**Example**: Longest substring without repeating characters
- Expand R to include new character
- Contract L to remove duplicates

### Pattern 3: Fast and Slow (Linked Lists)
```
1 -> 2 -> 3 -> 4 -> 5 -> 6
slow: 1, fast: 1
```

**Mental Process:**
1. Both start at head
2. Slow moves 1 step, fast moves 2 steps
3. If they meet → cycle exists
4. If fast reaches end → no cycle

## Step-by-Step Mental Framework

### Step 1: Identify the Pattern
Ask yourself:
- Is the data sorted? → Opposite ends pattern
- Do I need to find a window/subarray? → Same direction pattern
- Is it a linked list with potential cycles? → Fast/slow pattern

### Step 2: Define Pointer Roles
- **What does each pointer represent?**
- **What conditions determine their movement?**
- **What's the termination condition?**

### Step 3: Handle Edge Cases
- Empty array/list
- Single element
- All elements same
- No valid solution exists

### Step 4: Track State
- What information do you need to maintain?
- How do you update it when pointers move?

## Common Pitfalls & Mental Checks

### 1. **Off-by-One Errors**
- **Mental Check**: "Did I consider the case where pointers meet?"
- **Solution**: Always verify termination condition

### 2. **Infinite Loops**
- **Mental Check**: "Will my pointers always move?"
- **Solution**: Ensure at least one pointer moves in each iteration

### 3. **Missing Edge Cases**
- **Mental Check**: "What if array is empty/single element?"
- **Solution**: Handle base cases explicitly

### 4. **Wrong Pointer Movement**
- **Mental Check**: "Am I moving the right pointer for the right reason?"
- **Solution**: Double-check your movement logic

## Problem-Solving Template

### 1. **Opposite Ends Template**
```python
def two_pointers_opposite_ends(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:  # or left <= right depending on problem
        # Process current elements
        if condition_met:
            # Update result
            left += 1  # or right -= 1
        elif need_smaller:
            right -= 1
        else:
            left += 1
    
    return result
```

### 2. **Same Direction Template**
```python
def two_pointers_same_direction(arr):
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # Expand window
        while not valid_window(left, right):
            left += 1  # Contract window
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

## Key Insights for Mental Mastery

### 1. **Think in Terms of Invariants**
- What property must always be true?
- How do pointer movements maintain this property?

### 2. **Visualize the Process**
- Draw the array/list
- Mark pointer positions
- Trace through a few iterations

### 3. **Consider the Search Space**
- How much of the search space can you eliminate with each comparison?
- Are you making optimal use of the sorted property?

### 4. **Think About Convergence**
- Will your pointers eventually meet?
- What guarantees termination?

## Practice Problems by Pattern

### Opposite Ends:
- Two Sum II (sorted array)
- Container With Most Water
- 3Sum
- Valid Palindrome

### Same Direction:
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Remove Duplicates from Sorted Array
- Trapping Rain Water

### Fast/Slow:
- Linked List Cycle Detection
- Find Middle of Linked List
- Remove Nth Node From End of List

## Mental Checklist for Two Pointer Problems

- [ ] Is the data structure suitable for two pointers?
- [ ] Have I identified the correct pattern?
- [ ] Are my pointer movement conditions correct?
- [ ] Have I handled all edge cases?
- [ ] Will my algorithm terminate?
- [ ] Am I maintaining the correct state/invariants?
- [ ] Is my time complexity optimal?

## Advanced Mental Models

### 1. **Binary Search Analogy**
Think of opposite ends as binary search on steroids - instead of eliminating half the space, you're eliminating one element at a time but with more information.

### 2. **Sliding Window Intuition**
Same direction pointers create a "window" that expands and contracts based on conditions - like adjusting a camera lens to focus on the right subject.

### 3. **Race Analogy**
Fast/slow pointers are like a race where the fast runner will eventually lap the slow runner if there's a circular track (cycle).

## Conclusion

Two pointers is fundamentally about **efficient traversal** and **eliminating unnecessary work**. The key is to:
1. Identify when the technique applies
2. Choose the right pattern
3. Define clear movement conditions
4. Handle edge cases properly

With practice, you'll develop an intuition for when and how to apply two pointers, making it one of your most powerful algorithmic tools. 