from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next      
class MakeListNode:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.node = self._create_list_node()

    def _create_list_node(self):
        if not self.nums: return None
        head = ListNode(self.nums[0])
        current = head
        for num in self.nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head
    
    @property
    def head(self):
        return self.node
    
    def print_list_node(self, node=None):
        if node: 
            current = node
        else: 
            current = self.head
        while current:
            print(current.val)
            current = current.next

if __name__ == '__main__':
    
    nums = [1,2,3,4,5]
    link_list_obj = MakeListNode(nums=nums)
    head = link_list_obj.head
    link_list_obj.print_list_node()