# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

class Solution:
    def tribonacci(self, n: int) -> int:
        results = [] 
        
        for i in range(n+1):
            if i==0:
                results.append(0)
            elif i in (1, 2):
                results.append(1)
            else:
                # print("i: ", i)
                results = results[-3:]
                # print(results)
                tibo = sum(results)
                results.append(tibo)
        return results.pop() if results else 0

obj = Solution()
result = obj.tribonacci(25)
print(result)