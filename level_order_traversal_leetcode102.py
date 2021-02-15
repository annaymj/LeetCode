```
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque()
        
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
            
            res.append(level)
        
        return res
                        
