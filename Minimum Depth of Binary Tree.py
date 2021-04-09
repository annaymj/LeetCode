```
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        dq = deque()
        dq.append(root)
        depth = 1
        
        while len(dq) > 0:
            for i in range(len(dq)): # len(dq) could be 1 or 2, depends on the number of child
                currNode = dq.popleft()
               
                if currNode.left is not None:
                    dq.append(currNode.left)
                if currNode.right is not None:
                    dq.append(currNode.right)
                elif currNode.left is None and currNode.right is None: # if a leaf node is found
                    return depth 
                
            depth += 1 # increase depth at each level
                
            
            
    
