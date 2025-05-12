#1. Two Sum
#https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
sol = Solution()

nums = [1,2,3,4]
target = 5
print(sol.twoSum(nums, target))

