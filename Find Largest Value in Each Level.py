```
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,null,2]
Output: [1,2]

Example 5:
Input: root = []
Output: []
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        q = deque()
        res = [] # a list to store the max value for each level
        
        if root: 
            q.append(root)
        
        while q: # keep pop left of q till empty
            level, size = [], len(q) # level is a list of node values at a that level
            
            # pop the current element, store the value in levels, loop through the children and append value to deque q
            for i in range(size):
                node = q.popleft() # deque popleft is O(1)
                level.append(node.val)
                
                if node.left is not None: 
                    q.append(node.left)
                    
                if node.right is not None:
                    q.append(node.right)
            
            res.append(max(level))
        return res
            
        
        
