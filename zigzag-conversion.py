# The string "PAYPALISHIRING" is written in a zigzag pattern \
# on a given number of rows like this: 
#     (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
 

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        ans = ['']*numRows
        print(ans)
        rows = 0
        increament = 1
        while s:
            if rows == numRows:
                rows = numRows-2
                increament = -1
            elif rows == -1: 
                rows = 1
                increament = 1
                
            c = s[0]
            ans[rows] +=c
            s = s[1:]
            rows +=increament
            
        return "".join(ans)

obj = Solution()
# result = obj.convert(s = "PAYPALISHIRING", numRows = 4)
result = obj.convert(s = "ABC", numRows = 1)
print(result)
            