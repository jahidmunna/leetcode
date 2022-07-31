# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        output = sorted(count.items(), key=lambda x: x[1], reverse=True)[0][0]
        
        return output
        
        
        


obj = Solution()
print(obj.majorityElement([2,2,1,1,1,2,2]))