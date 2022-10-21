# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
from typing import List
from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        q = deque()        
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
            q.append(num)
            
            if len(seen) == k+1:
                seen.remove(q.popleft())
            
            # print(f"{num=}\t{q=}\t{seen=}")
            
        
        return False


obj = Solution()
# result = obj.containsNearbyDuplicate(nums=[1,2,3,1,2,3], k = 2) # False
result = obj.containsNearbyDuplicate(nums=[1,2,5,7,8,2,1], k = 4) # True
print(result) # False