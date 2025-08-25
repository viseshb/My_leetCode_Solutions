#https://leetcode.com/problems/sqrtx/description/
'''69. Sqrt(x)
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1'''

class Solution:
    def sqrt(self, x: int):
        if x < 0:
            return False
        if x < 2:
            return x
        lo, hi =1, x//2 +1
        while lo< hi:
            mid = (lo + hi)//2
            if mid*mid <=x:
                lo = mid + 1
            else:
                hi = mid
        return lo -1

s = Solution()
print(s.sqrt(x = 49))                
