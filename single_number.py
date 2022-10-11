# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = dict(Counter(nums))
        # output = sorted(count.items(), key=lambda x: x[1])[0][0]
        # return output
        # best approach XOR, O(n), S(1)
        ans = 0 
        for num in nums:
            ans ^=num
        return ans        
        
        


obj = Solution()
print(obj.singleNumber([4,1,2,1,2]))