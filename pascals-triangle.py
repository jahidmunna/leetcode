# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for r in range(numRows):
            temp = []
            if r in (0,1):
                temp = [1]*(r+1)
            else:
                for i in range(r+1):
                    # print('prev_rows: ',prev_rows)
                    prev_rows = result[r-1]
                    if i in (0,r):
                        temp += [1]
                    else:
                        prev_val = prev_rows[i-1] + prev_rows[i]
                        temp.append(prev_val)
            result.append(temp)
            # print(result)
        return result


obj = Solution()
result = obj.generate(numRows = 5)

print(result)
                
                
                