# Given the root of a Binary Search Tree and a target number k, 
# return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
#             5
#         3       5
#     2       4|None  7
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
#         5
#     3       6
# 2       4|None  7
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if not root: return False
        
        queue = deque([root])
        seen = set()
        while queue:
            node = queue.popleft()
            if node:
                num1 = node.val
                num2 = k - num1
                if num2 in seen:
                    return True
                seen.add(num1)

                queue.append(node.left)
                queue.append(node.right)
                
        return False

# root = [5,3,6,2,4,null,7], k = 9 # True

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right.right = TreeNode(7)


obj = Solution()
result = obj.findTarget(root=root, k=9)
print(result)