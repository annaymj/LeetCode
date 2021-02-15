```
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        if node is None:
            return
        
        # add the current node the path's list
        pathNodes.append(node.val)
        
        # check if the curernt node is a leaf node
        if remainingSum == node.val and node.left is None and node.right is None:
            pathsList.append(list(pathNodes))
        else:
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
        
        # pop th node once done processing all of it's children
        pathNodes.pop()
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        pathsList = []
        pathNodes = []
        self.recurseTree(root, targetSum, pathNodes, pathsList)
        
        return pathsList
