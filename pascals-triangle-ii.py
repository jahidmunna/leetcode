# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # resulting in 2D array, initialize all with 1
        result = [[1]*(rowIndex+1)]*(rowIndex+1)
        
        for row in range(1, rowIndex+1):
            temp = result[row][:row+1]
            for col in range(1, row):
                result[row][col] = temp[col] + temp[col-1]
            
            del temp
                        
        return result[rowIndex]


obj = Solution()

# print(obj.getRow(0))
# print(obj.getRow(1))
# print(obj.getRow(2))
# print(obj.getRow(3))
print(obj.getRow(4))
