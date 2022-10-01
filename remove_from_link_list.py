# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        # print(head.val)
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next =  self.removeElements(head.next, val)
        return head

       

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)



def print_node(head):
    current = head
    while current:
        print(current.val)
        current = current.next

obj = Solution()
result = obj.removeElements(head=head, val=6)
if result:
    print_node(result)
