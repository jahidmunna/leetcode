# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

#  Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, string: str) -> str:
        
        # Add special characters to the string to avoid palindromes of even length
        modified_string = "#".join("^{}$".format(string))
        length = len(modified_string)
        palindrome_radii = {}
        center = 0
        right_boundary = 0
        
        for i in range(1, length - 1):
            mirror_index = 2 * center - i
            
            # Check if palindrome at i can expand past right boundary
            if right_boundary > i and i in palindrome_radii:
                palindrome_radii[i] = min(right_boundary - i, palindrome_radii[mirror_index])
            else:
                palindrome_radii[i] = 0
            
            # Expand palindrome centered at i
            try:
                while modified_string[i + 1 + palindrome_radii[i]] == modified_string[i - 1 - palindrome_radii[i]]:
                    palindrome_radii[i] += 1
            except IndexError:
                pass
            
            # Update center and right boundary if palindrome at i expands past right boundary
            if i + palindrome_radii[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radii[i]
        
        # Find the longest palindrome
        max_length, center_index = max((palindrome_radii[i], i) for i in palindrome_radii)
        start = (center_index - max_length) // 2
        end = (center_index + max_length) // 2
        return string[start : end]


obj = Solution()
result = obj.longestPalindrome("forgeeksskeegfor") 

print(result) #geeksskeeg