"""

88. Merge Sorted Array
Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 to form one sorted array.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""

def merge(nums1, m, nums2, n):
    # Your solution here

    ptr_to_fill = m + n - 1
    m = m - 1
    n = n - 1

    while ptr_to_fill >= 0:

        if m < 0:
            nums1[ptr_to_fill] = nums2[n]
            n -= 1
        elif n < 0:
            nums1[ptr_to_fill] = nums1[m]
            m -= 1
        else:
            if nums1[m] < nums2[n]:
                nums1[ptr_to_fill] = nums2[n]
                n -= 1
            else:
                nums1[ptr_to_fill] = nums1[m]
                m -= 1
        ptr_to_fill -= 1

# Test cases
def test_merge():
    # Test case 1: Basic merge
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Test 1: {nums1[:m+n]}")  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test case 2: nums2 is empty
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(f"Test 2: {nums1[:m+n]}")  # Expected: [1]
    
    # Test case 3: nums1 is empty
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Test 3: {nums1[:m+n]}")  # Expected: [1]
    
    # Test case 4: nums1 has larger elements
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Test 4: {nums1[:m+n]}")  # Expected: [1, 2, 3, 4, 5, 6]
    
    # Test case 5: nums2 has larger elements
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Test 5: {nums1[:m+n]}")  # Expected: [1, 2, 3, 4, 5, 6]
    
    # Test case 6: Single element arrays
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(f"Test 6: {nums1[:m+n]}")  # Expected: [1, 2]

if __name__ == "__main__":
    test_merge()