#217 Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/
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