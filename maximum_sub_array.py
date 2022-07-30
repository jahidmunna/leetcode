# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23


from typing import List

# Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dynamic_array = [nums[0]]
        for i, num in enumerate(nums[1:], 1):
            max_num = max(num+dynamic_array[i-1], num)
            dynamic_array.append(max_num)

        return max(dynamic_array)



obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
