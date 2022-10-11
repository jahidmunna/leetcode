# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, 
# return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        s,e = 0, l-1
        while s<=e:
            m = int((s+e)/2)
            prev = (m-1+l)%l
            next = (m+1)%l
            
            current_num = nums[m]
            next_num, prev_num = nums[next], nums[prev]
            # print(f"current: {current_num}\tnext: {next_num}\tprev: {prev_num}")
            if current_num<=prev_num and current_num<=next_num:
                return current_num
            elif current_num<=nums[e]:
                e = m-1
            else:
                s = m+1
        return -1

obj = Solution()
result = obj.findMin([4,5,6,7,0,1,2])
print(result)