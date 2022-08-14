from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.verbose = False
    
    def add(self, val):
        if self.verbose: print("Adding node with value {}".format(val))
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def remove(self, val):
        node = self.head
        prev = None
        while node:
            if node.val == val:
                if node == self.head:
                    self.head = self.head.next
                    prev = self.head
                if node == self.tail:
                    self.tail = prev
                    self.tail.next = None
                else:
                    node.val = node.next.val
                    node.next = node.next.next
                if self.verbose: print("Deleted node with value {}".format(val))
                return
            prev = node
            node = node.next
        
        if self.verbose: print("node with value {} not found".format(val))
        
    def sort(self):
        if self.head:
            current = self.head
             
            while current.next:
                
                travel = current
                min_node = travel
                
                while(travel):
                    if travel.val < min_node.val:
                        min_node = travel
                    
                    travel = travel.next
                
                current.val, min_node.val = min_node.val, current.val
                    
                current = current.next                                      
                    

    
    def print(self):
        if self.verbose: print("Printing linked list")
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next
        print()
    
    
if __name__ == '__main__':    
    linked_list = LinkedList()
    
    linked_list.add(5)
    linked_list.add(4)
    # linked_list.print()
    # linked_list.remove(4)
    # linked_list.remove(10)
    # linked_list.print()
    linked_list.add(2)
    linked_list.add(15)
    linked_list.add(10)
    linked_list.add(10)
    print("before sorting")
    linked_list.print()
    print("Sorting linked list")
    linked_list.sort()
    linked_list.print()
    

    