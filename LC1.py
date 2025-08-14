#https://leetcode.com/problems/two-sum/description/
'''1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

 
'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

from typing import List, Tuple
#O[n^2] Approach 
class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None                            
#O[n] Approach    
class Solution2:   
    def twoSum(self, nums:List[int], target: int)-> List[int]:
        map = {}
        for i , num in enumerate(nums):
            if target - num in map:
                return [map[target-num], i]
            else:
                map[num] = i

#O[n^log(n)] Approach for sorted List
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums [right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left +=1
            else:
                right -=1
        return None            

# O(n log n) Approach for unsorted list using .sort()
class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = [(v, i) for i, v in enumerate(nums)]
        a.sort(key=lambda x: x[0])
        l, r = 0, len(a) - 1
        while l < r:
            s = a[l][0] + a[r][0]
            if s == target:
                return sorted([a[l][1], a[r][1]])
            elif s < target:
                l += 1
            else:
                r -= 1
        return []

# O(n log n) Approach for unsorted list using custom Merge Sort
class Solution5:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr: List[Tuple[int, int]] = [(v, i) for i, v in enumerate(nums)]

        def msort(a):
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            L, R = msort(a[:mid]), msort(a[mid:])
            i = j = 0
            out = []
            while i < len(L) and j < len(R):
                if L[i][0] <= R[j][0]:
                    out.append(L[i]); i += 1
                else:
                    out.append(R[j]); j += 1
            out.extend(L[i:]); out.extend(R[j:])
            return out

        a = msort(arr)
        l, r = 0, len(a) - 1
        while l < r:
            s = a[l][0] + a[r][0]
            if s == target:
                return sorted([a[l][1], a[r][1]])
            elif s < target:
                l += 1
            else:
                r -= 1
        return []

              
# --------------------
# Test Runs
# --------------------


print(Solution().twoSum([2, 7, 11, 15], 9))     
print(Solution2().twoSum([2, 7, 11, 15], 9))    
print(Solution3().twoSum([2, 7, 11, 15], 9))  
print(Solution4().twoSum([7, 2, 11, 15], 9))  
print(Solution5().twoSum([7, 11, 2, 15], 9))  