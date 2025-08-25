#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
'''28. Find the Index of the First Occurrence in a String
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)- len(needle) + 1):
            if needle == haystack[i : i + len(needle)]:
                return i
        return -1   
    
testcases = [
    ("sadbutsad", "sad", 0),        # appears at 0 (and also 6, but first is 0)
    ("hello", "ll", 2),             # "ll" starts at index 2
    ("aaaaa", "bba", -1),           # not found
    ("abc", "", 0),                 # empty needle -> 0
    ("a", "a", 0),                  # single char match
    ("a", "aa", -1),                # needle longer than haystack
    ("mississippi", "iss", 1),      # "iss" first at index 1
    ("mississippi", "issi", 1),     # "issi" first at index 1
    ("mississippi", "sipp", 6),     # "sipp" starts at index 6
    ("leetcode", "leeto", -1)       # not found
]

s = Solution()
for i , (haystack, needle, expected) in enumerate(testcases):
    result = s.strStr(haystack, needle)
    print(f"Testcase {i}: haystack='{haystack}', needle='{needle}' => result={result}, expected={expected}")