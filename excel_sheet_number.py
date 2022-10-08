# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle:
            return 0
        ans = 0
        for c in columnTitle:
            num = ord(c) - 64
            ans = ans*26 + num
        return ans


obj = Solution()
result = obj.titleToNumber("ZY")

print(result)
