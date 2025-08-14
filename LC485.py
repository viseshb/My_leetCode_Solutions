#485. Max Consecutive Ones (LeetCode Array Question)
#https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def FindMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return False
        
        count = 0
        count_max = 0
        for num in nums:
            if num == 1:
                count +=1
                count_max = max(count_max,count)
            else:
                count = 0

        return count_max



nums = list(map(int, input("Enter the array: ").split()))
result = Solution()
print(result.FindMaxConsecutiveOnes(nums))

