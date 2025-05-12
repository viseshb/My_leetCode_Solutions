#9. Palindrome Number
#https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        

        num_str = str(x)
        return num_str == num_str[::-1]
    
result = Solution()
x = int(input("Enter the Number:"))
print(result.isPalindrome(x))


    