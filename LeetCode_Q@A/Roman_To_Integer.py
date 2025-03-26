#13. Roman to Integer
#https://leetcode.com/problems/roman-to-integer/description/

def romanToInteger(s: str)-> int:
    roman  = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total = total - roman[s[i]]
        else:
            total = total + roman[s[i]]
    return total      

s = 'XXXVV'
val = romanToInteger(s)
print("The value is:", val)