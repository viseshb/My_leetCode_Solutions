#217 Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/
'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def contains_Duplicates(self, nums):
        seen = set()
        for num in nums:
            if num in seen:      # duplicate found
               return True
            seen.add(num)        # mark number as seen
        return False  


sol = Solution()


test_cases = [([1,2,3,4],False),
              ([1,1,1,2,3,4], True),
              ([19,8,7,6], False),
              ([1,1,1,1], True)]

for i , (nums, expected) in enumerate(test_cases):
    result = sol.contains_Duplicates(nums)
    print(f"Test Case {i}: input = {nums}, expected = {expected}, got = {result}")