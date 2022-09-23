# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def topView(self, root: Optional[TreeNode]) -> List[int]:
      # fill out left side
      stake_left = []
      current = root
      while current:
         if current:
            stake_left.append(current.val)   
         current = current.left
      
      # fill out right side
      queue_right = deque()
      current = root.right
      while current:
         if current:
            queue_right.append(current.val)   
         current = current.right
                   
      value = []
      while stake_left:
         val = stake_left.pop()
         value.append(val)
      
      while queue_right:
         val = queue_right.popleft()
         value.append(val)
      
      return value
             
# input:
   # 	1
# 	 2    3
# 4   5      6 
# Would return {4, 2, 1, 3, 6}

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(6)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

obj = Solution()
result = obj.topView(root=root)

print(result)