```
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def findDepth(self, node:TreeNode):
        if node is None:
            return 0
        l_depth = self.findDepth(node.left)
        r_depth = self.findDepth(node.right)
        self.diamater = max(self.diamater,l_depth + r_depth +1)
        return max(l_depth,r_depth) + 1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diamater = 1
        self.findDepth(root)
        return self.diamater - 1
        
        
        
