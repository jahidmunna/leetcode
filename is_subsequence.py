# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = ".*".join(list(s))
        pattern = r'^.*{}.*$'.format(s)
        match = re.match(pattern, t)
        if match:
            return True 
        return False

test = Solution()
# print(test.isSubsequence(s = "abc", t = "ahbgdc"))
print(test.isSubsequence(s = "axc", t = "ahbgdc"))

        