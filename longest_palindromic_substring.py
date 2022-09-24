# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

#  Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(s):
            return s == s[::-1]
        
        indexes = defaultdict(list)
        max_langth = 1
        palindrome = s[0]
        for i, c in enumerate (s):
            if c not in indexes:
                indexes[c].append(i)
            else:
                for idx in indexes[c]:
                    string = s[idx:i+1]
                    if isPalindrome(string):
                        if max_langth < len(string):
                            max_langth = len(string)
                            palindrome = string
                            break
                indexes[c].append(i)
        
        del indexes, max_langth
    
        return palindrome


obj = Solution()
result = obj.longestPalindrome("aba")

print(result)