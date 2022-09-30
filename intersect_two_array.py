# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = dict(Counter(nums1))
        nums2 = dict(Counter(nums2))
        set1 = set(nums1.keys())
        set2 = set(nums2.keys())
        intersects = list(set1.intersection(set2))
        result = []
        for intersect in intersects: 
            min_times = min(nums1[intersect], nums2[intersect])
            result += [intersect]*min_times
        
        return result
        
        

obj = Solution()
result = obj.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(result)