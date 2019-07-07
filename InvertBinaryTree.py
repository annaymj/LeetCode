# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:05:01 2019

@author: annayu

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        tmp  = root.right
        root.right = root.left
        root.left = tmp
        
        self.invertTree(root.left) 
        self.invertTree(root.right)
        return root