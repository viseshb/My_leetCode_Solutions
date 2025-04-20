#217 Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def contains_Duplicates(self, nums):
        my_dict = {}
        my_duplicates = []

        for i in nums:
            if i in my_dict:
                my_dict[i] +=1
            else:
                my_dict[i] = 1

        for j in my_dict:
            if my_dict[j] > 1:
                my_duplicates.append(j)
        return my_duplicates        


sol = Solution()
nums = [1,2,3,4,2,5,3,3,4,5]

print(sol.contains_Duplicates(nums))

