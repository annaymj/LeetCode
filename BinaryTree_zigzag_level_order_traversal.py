```
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque()
        level_index = 0
        
        if root:
            q.append(root)
        
        while len(q) > 0:
            level, size = [], len(q) # use list level to store node values at that level
            
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
            
            # check the level index is even or odd
            if level_index %2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            
            level_index += 1
        
        return res
                
            
        
   
        
        
        
