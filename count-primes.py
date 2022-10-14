# Given an integer n, 
# return the number of prime numbers that are strictly less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0
from math import ceil, sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0
        
        prime = [True]*n
        
        prime[0] = False
        prime[1] = False
        
        for i in range(4, n, 2):
            prime[i] = False
        
        for i in range(6, n, 3):
            prime[i] = False

        limit = ceil(sqrt(n))
        
        for i in range(3, limit+1):
            if prime[i]:
                j = 2
                while j*i<n:
                    prime[j*i] = False
                    j +=1
        
        return sum(prime)
    

obj = Solution(5000000)
result = obj.countPrimes()