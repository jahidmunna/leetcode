from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None) -> None:
        self.root = root
    
    def bfs(self):
        graph = deque()
        graph.append(self.root)
        while  graph:
            node = graph.popleft()
            if node:
                print(node.val)
            if node.left:
                graph.append(node.left)
            if node.right:
                graph.append(node.right)
    
    def dfs(self):
        def apply(node):
            if node:
                print(node.val)
                apply(node.left)
                apply(node.right)
        
        apply(self.root)
            
    def preorder_travel(self):
        def travel(node):
            if node:
                print(node.val, end="\t")
                travel(node.left)
                travel(node.right)
        if self.root:
            travel(self.root)
    
    def inorder_travel(self):
        def travel(node):
            if node:
                travel(node.left)
                print(node.val, end="\t")
                travel(node.right)
        if self.root:
            travel(self.root)
    
    def postorder_travel(self):
        def travel(node):
            if node:
                travel(node.left)
                travel(node.right)
                print(node.val, end="\t")

        if self.root:
            travel(self.root)
            

#      1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


tree = Tree(root)
# print("Pre-Order")
# tree.preorder_travel() # 1 2 4 5 3
# print()
# print("-"*50)
# print("Order")
# tree.inorder_travel() # 4 2 5 1 3
# print()
# print("-"*50)
# print("Post-Order") # 4 5 2 3 1
# tree.postorder_travel()
# print()
# print("-"*50)

tree.bfs() # 1, 2, 3, 4, 5
