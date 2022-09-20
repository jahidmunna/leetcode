# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# Example 1:
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

# Example 2:
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = ''.join([chr(x) for x in nums2])
        strmax = ''
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in nums2:
                ans = max(ans,len(strmax))
            else:
                strmax = strmax[1:]
        return ans
                

        



obj = Solution()
result = obj.findLength([1,2,3,2,1], [3,2,1,4,7])
# result = obj.findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0])
# result = obj.findLength(nums1 = [0,0,0,0,1], nums2 = [1,0,0,0,0])
# result = obj.findLength(nums1 = [70,39,25,40,7], nums2 = [52,20,67,5,31])

print(result)