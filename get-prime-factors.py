# Given an int n, return all of it's prime factor

# Example 1: 
# input: n = 630
# output: [2, 3, 3, 5, 7]
# Explanation: 2 * 3 * 3 * 5 * 7 = 630

# Example 2:
# input: n = 13
# output: [13]

# Eample 3:
# input: n = 10 
# output = [2 , 5]

from typing import List 
def get_prime_factors(n: int) -> List[int]:
    results = []
    i = 2
    while n>1:
        if n%i == 0:
            results.append(i)
            n = n//i
        else:
            i +=1
        # print(results, "=>", n)
    return results

print(get_prime_factors(12))