# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:39:29 2019

@author: annayu

Given the root of a binary search tree with distinct values, modify it so that 
every node has a new value equal to the sum of the values of the original tree 
that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        
        def dfs(node):
            nonlocal total
            if not node:
                return
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
        
        dfs(root)
        return root