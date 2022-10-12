# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return None
        size = 0
        current = head
        while current:
            size +=1
            current = current.next

        remove_index = size - n
        
        current = head
        i = 0 
        while current:
            if i == remove_index-1:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
            else:
                current = current.next
            i +=1
            
        return head
                       
from make_list_node import MakeListNode
link_list_obj = MakeListNode(nums=[1,2,3,4,5])
head = link_list_obj.head

obj = Solution()
result = obj.removeNthFromEnd(head, 2)

link_list_obj.print_list_node(node=result)
