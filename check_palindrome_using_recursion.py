# check if a string is palindrom or not using recursion

class Solution:
    def isPalindrome(self, s: str) ->bool:
        if not s:
            return True
        if s[0] != s[-1]:
            return False
        print(s)
        return self.isPalindrome(s[1:-1])

obj = Solution()
result = obj.isPalindrome(s = "abcbad")
print(result)
