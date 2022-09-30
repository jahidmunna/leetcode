# Given the root of a binary tree, 
# return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example:
#         1
#     2       3
# 4               5
# input = 
# result = [[1], [2,3], [4,5]]

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        seen = set()
        results = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.popleft()
                if not node in seen and node:
                    seen.add(node)
                    if node.val != None:
                        # print(node.val) 
                        temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                            
            if temp: results.append(temp)
        
        return results


# [1,2,3,4,None,None,5]
root = TreeNode(1)
# level 1
root.left = TreeNode(2)
root.right = TreeNode(3)
# level 2 Left
root.left.left = TreeNode(4)
root.left.right = TreeNode(None)
# level 2 Right
root.right.left = TreeNode(None)
root.right.right = TreeNode(5)


obj = Solution()
result = obj.levelOrder(root=root)
print(result)