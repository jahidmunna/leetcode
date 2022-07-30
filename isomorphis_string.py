# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

from genericpath import exists
from typing import List

# class Solution:        
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         # if does not matched with length means they are mapping with different/multiple characters
#         if len(s)!=len(t):
#             return False
        
#         char_map = dict() 
        
            
#         for c1, c2 in zip(s,t):
#             print(c1, c2, char_map, sep="\t")
#             if c1 in char_map and c2 in char_map:
#                 if c2 !=char_map[c1] or c1 != char_map[c2]:
#                     print(f"does not matched with: {c1}: {char_map[c1]}\t{c2}: {char_map[c2]}")
#                     return False
#             elif c1 not in char_map and c2 not in char_map:
#                 print("Not exit")
#                 char_map[c1] = c2
#                 char_map[c2] = c1
#             elif c1 in char_map and c2 not in char_map:
#                 print(f"{c1} exit {c2} not")
#                 return False
#             elif c2 in char_map and c1 not in char_map:
#                 print(f"{c2} exit {c1} not")
#                 return False
            
#         return True                

class Solution:        
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if does not matched with length means they are mapping with different/multiple characters
        if len(s)!=len(t):
            return False
        
        # mapping dictionary
        char_map = dict() 
        
        for c1, c2 in zip(s,t):
            # if c1 exists in the dictonary, but the mapping values does not matched return false
            if c1 in char_map:
                if c2 != char_map[c1]:
                    return False
            # if c1 doest not exist in the dictonary, but c2 already mapped with other key means one char is mapped with multiple char, so, return false
            elif c2 in char_map.values():
                return False
            else:
                # if c1 doest not exist in the dictonary, add to the dictonary
                if c1 == c2:
                    # for same mapping key and value
                    char_map[c1] = c1
                else:  
                    # for different key with value
                    char_map[c1] = c2
        return True  
    
obj = Solution()
print(obj.isIsomorphic(s = "egg", t = "add")) # True
print(obj.isIsomorphic(s = "foo", t = "bar")) # Flase
print(obj.isIsomorphic(s = "paper", t = "title")) # True
print(obj.isIsomorphic(s = "badc", t = "baba")) # False
print(obj.isIsomorphic(s = "bbbaaaba", t = "aaabbbba")) # False


