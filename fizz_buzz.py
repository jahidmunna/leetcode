# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = range(1, n+1)
        result = list(map(
                        lambda x: 
                              "FizzBuzz" if x % 5 == 0 and x % 3 ==0 
                              else "Fizz" if x % 3 == 0 
                              else "Buzz" if x % 5 == 0 
                              else str(x), 
                        result
                    ))

        return result

obj = Solution()
result = obj.fizzBuzz(n=15)

print(result)