# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false
 
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.


class Solution:
    
    @staticmethod
    def isPalindrome(str, s, e):
        while s<e:
            if str[s]!= str[e]:
                return False
            s +=1
            e -=1 
        return True 
    
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        size = len(s)
        start = 0 
        end = size-1
        while start < end:
            if s[start] != s[end]:
                if(Solution.isPalindrome(s, start+1, end) or Solution.isPalindrome(s, start, end-1)):
                    return True
                else:
                    return False
            start +=1 
            end -=1
                
        return True
    

obj = Solution()
# result = obj.validPalindrome("abdcca")
# result = obj.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") #True
# result = obj.validPalindrome("ebcbbececabbacecbbcbe") # True
result = obj.validPalindrome("eeccccbebaeeabebccceea") # False
print(result)


