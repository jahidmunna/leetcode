# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        max_length = 0
        for c in s:
            if c in seen:
                i = seen.index(c)
                seen = seen[i+1:]
                # seen.clear()
            seen.append(c)
            max_length = max(max_length, len(seen))
        del seen
        return max_length
    
    

obj = Solution()
# result = obj.lengthOfLongestSubstring('abcabcbb')
# result = obj.lengthOfLongestSubstring('aab')
result = obj.lengthOfLongestSubstring('dvdf')


print(result)
