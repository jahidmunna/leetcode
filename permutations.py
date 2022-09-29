# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

from typing import List 
from itertools import permutations as per 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list(per(nums))
        
        result = list(map(list, result))
        
        return result


obj = Solution()
# result = obj.permute([1,2,3])
result = obj.permute([1])
print(result)
