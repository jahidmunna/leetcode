# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.


# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []


from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = [] 
        queue = deque([root])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                print(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            print(node.val)
            print("-"*50)
            result.append(node.val)
        
        return result
            


# input:
    #         1
    #     2       3
    # 4       5|8   
    #     7|0
# Would return [1, 3, 8, 0]

root = TreeNode(1)
# RIGHT SIDE
root.right = TreeNode(3)
root.right.left = TreeNode(8)
# LEFT SIDE
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.right = TreeNode(7)
root.left.right.left = TreeNode(0)

obj = Solution()
result = obj.rightSideView(root=root)

print(result)