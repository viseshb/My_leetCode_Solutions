#1941. Check if All Characters Have Equal Number of Occurrences
#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table

# def areOccurrencesEqual( s: str) -> bool:
#         my_dict = {}
#         count = 0
#         for string in s:  
#             if string in my_dict:
#                 my_dict[string] +=1
#             else:
#                 my_dict[string] = 1    
        
#         frequencies = list(my_dict.values())

#         first = frequencies[0]

#         for count in frequencies:
#             if count == first:
#                 return True
#         return False     
# OR their is a simple code for it as well


def areOccurrencesEqual( s: str) -> bool:
    my_dict = {}

    for string in s:
        my_dict[string] = my_dict.get(string, 0) + 1

    return len(set(my_dict.values())) == 1                


                            
            
        

s = "abcbac"

print(areOccurrencesEqual(s))