# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
# which is then converted into a different digit string.
# To determine how you "say" a digit string, 
# split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
# Then for each substring, say the number of digits, then say the digit. 
# Finally, concatenate every said digit.

# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "12

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def counter(s):
            if not s:
                return None
            if len(s)==1:
                return "1" + s
            result = []
            count, prev = 1, s[0]
            for c in s[1:]:
                if c == prev:
                    count +=1
                else:
                    result += [str(count), prev]
                    prev = c
                    count = 1
                    
            # For last character
            result += [str(count), prev]
            return "".join(result)
        
        prev_str = self.countAndSay(n-1)
        current_str = counter(prev_str)
        
        return current_str

obj = Solution()
result = obj.countAndSay(30)
print(result)