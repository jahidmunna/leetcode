# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent 
# and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. 
# It is guaranteed that the answer is unique.

 

# Example 1:
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
        
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        pair = (s[0],1)
        stack.append(pair)
        # print(stack)
        for c in s[1:]:
            if stack:     
                c2, num = stack.pop()
                if c == c2:
                    if num == k-1:
                        continue
                    else:
                        num +=1
                        pair = (c, num)
                        stack.append(pair)
                else:
                    pair = (c2, num)
                    stack.append(pair)
                    pair = (c, 1)
                    stack.append(pair)
            else:
                pair = (c, 1)
                stack.append(pair)
            # print(stack)
        
        if not stack:
            return ""
        ans = ""
        for c, num in stack:
            sub_str = c*num
            ans +=sub_str
        return  ans
    
obj = Solution()
# result = obj.removeDuplicates(s = "abcd", k = 2)
# result = obj.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)
result = obj.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
print(result)                
