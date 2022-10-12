# Given an integer array nums, 
# return the largest perimeter of a triangle with a non-zero area, 
# formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.

# Example 1:
# Input: nums = [2,1,2]
# Output: 5

# Example 2:
# Input: nums = [1,2,1]
# Output: 0
 
# Constraints:
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = sorted(nums, reverse = True)
        
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)
        
        print("nums: ",nums)
        return 0 if len(nums) < 3 else sum(nums[:3])

obj = Solution()
# result = obj.largestPerimeter(nums = [2,1,2])
result = obj.largestPerimeter(nums = [9, 5, 4, 4, 3])
print(result)