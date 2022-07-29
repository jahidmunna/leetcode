# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ob = Counter(nums)
        num_times = list(ob.values())

        result = list(filter((lambda x: x > 1), num_times))

        if result:
            return True

        return False


obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
print(obj.containsDuplicate([1, 2, 3, 4]))
print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
