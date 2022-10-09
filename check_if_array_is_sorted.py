# check if an array is sorted using recursion

from tabnanny import check
from typing import List

class Solution:
    def check_sorted(self, array: List) ->bool:
        if len(array) <= 1:
            return True
        if array[0] > array[1]:
            return False
        
        return self.check_sorted(array=array[1:])

obj = Solution()
result = obj.check_sorted(array=[1, 4, 3, 4])
print(result)
