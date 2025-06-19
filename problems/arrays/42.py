"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

def solution_1(height) -> int:

    if len(height) == 0 or len(height) == 1 or len(height) == 2:
        return 0
    
    l_max = [0] * len(height)
    r_max = [0] * len(height)

    m = height[0]

    for i in range(len(height)):
        m = max(m, height[i])
        l_max[i] = m
    
    m = height[len(height)-1]

    for i in range(len(height)-1, -1, -1):
        m = max(m, height[i])
        r_max[i] = m

    
    running_count = 0

    for i in range(len(height)):
        left = l_max[i]
        right = r_max[i]
        current = height[i]

        water = min(left, right) - current
        
        if water >= 0:
            running_count += water
    return running_count

print(solution_1([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution_1([4,2,0,3,2,5])) 