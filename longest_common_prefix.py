# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        prefix = strs[0]
        
        for str in strs:
            if prefix in str[:len(prefix)]:
                continue

            while prefix:
                if prefix in str[:len(prefix)]:
                    break
                prefix = prefix[:-1]
        
        return prefix


obj = Solution()
# result = obj.longestCommonPrefix(["flower","flow","flight"])
result = obj.longestCommonPrefix(["aca","cba"])
# result = obj.longestCommonPrefix(["dog","racecar","car"])

print(result)