from distutils.command.build import build
import numbers


class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    
    def insert(self, data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinaryTree(data)
        else:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinaryTree(data)
    
    
    def print_in_order(self):
        """
        In order
        """             
        if self.left:
            self.left.print_in_order()
        
        print(self.data)
        
        if self.right:
            self.right.print_in_order()
        


if __name__ == '__main__':
            
    def build_tree(elements):
        root = BinaryTree(data = elements[0])
        for num in elements[1:]:
            root.insert(num)
        
        return root
    
    
    numbers = [1, 10, 2, 123, 3, 5, 6, 7, 3, 2]
    
    btree = build_tree(numbers)
    
    btree.print_in_order()

        
    
               
            