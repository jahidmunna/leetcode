# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        result = []
        low, high = 0, len(nums) -1
        while low<=high:
            mid = int((low+high)/2)
            current = nums[mid]
            if current == target:
                result.append(mid)
                i = mid-1 
                j = mid +1
                size = len(nums) 
                while i>=0 or j<size:
                    if i>=0:
                        prev = nums[i]
                        if prev == target:
                            result.append(i)
                            i -=1
                        else: 
                            i = -1
                    if j<size:
                        next = nums[j]
                        if next == target:
                            result.append(j)
                            j +=1
                        else:
                            j = len(nums) 
            
                break 
            elif current < target:
                low = mid+1 
            else:
                high = mid -1
        return [min(result), max(result)] if result else [-1, -1]


obj = Solution()
# result = obj.searchRange(nums = [5,7,7,8,8,10], target = 8)
# result = obj.searchRange(nums = [5,7,7,8,8,10], target = 6)
# result = obj.searchRange(nums = [3, 3, 3], target = 3)
# result = obj.searchRange(nums = [1], target = 1)
result = obj.searchRange(nums = [2, 2], target = 2)

print(result)
