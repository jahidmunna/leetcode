# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example: 1
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from typing import Optional
from functools import reduce

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return []
        
        def get_value(root):
            values = []
            current = root
            while current:
                values.append(current.val)
                current = current.next
            
            return values[::-1]
        
        
        value1 = get_value(l1)
        value2 = get_value(l2)
        
        value1 = reduce(lambda x,y: x*10+y, value1)
        value2 = reduce(lambda x,y: x*10+y, value2)
        
        result = value1 + value2
        
        print(f"l1: {l1}")

        print(f"value1: {value1}")
        print(f"value2: {value2}")
        print(f"result: {result}")
        
        result = str(result)[::-1]
        
        result_node = ListNode(val= result[0])
        current_node = result_node
        for n in result[1:]:
            new_node = ListNode(val= n)
            current_node.next = new_node
            current_node = current_node.next
        
        print(f"result_node: {result_node}")
        return result_node
    