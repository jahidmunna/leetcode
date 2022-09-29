# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.


# Input : 
#                  1
#                /   \
#               2     3
#              / \     \
#             4   5     6             
# Output : 1 2 4

# Input :
#         1
#       /   \
#     2       3
#       \   
#         4  
#           \
#             5
#              \
#                6
# Output :1 2 4 5 6


from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = [] 
        queue = deque([root])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                # print(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
            # print(node.val)
            # print("-"*50)
            result.append(node.val)
        
        return result
            


# input:
    #         10
    #     2       3
    # 7       8|12  15   
    #             |14
# Would return [10, 2, 7, 14]

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(8)
root.right.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right.left = TreeNode(14)  

obj = Solution()
result = obj.leftSideView(root=root)

print(result)