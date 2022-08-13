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
    
    def add(self, val):
        print("Adding node with value {}".format(val))
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
                print("Deleted node with value {}".format(val))
                return
            prev = node
            node = node.next
        
        print("node with value {} not found".format(val))
    
    def print(self):
        print("Printing linked list")
        node = self.head
        while node:
            print(node.val, end=' ')
            node = node.next
        print()
    
    
if __name__ == '__main__':    
    linked_list = LinkedList()
    
    linked_list.add(5)
    linked_list.add(4)
    linked_list.print()
    linked_list.remove(4)
    linked_list.remove(10)
    linked_list.print()
    linked_list.add(2)
    linked_list.add(10)
    linked_list.add(15)
    linked_list.print()
    

    