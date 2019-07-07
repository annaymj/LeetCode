# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:46:45 2019

@author: annayu

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.


Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

"""

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        parent_x, depth_x = self.isCousinsHelper(root, x, 0)
        parent_y, depth_y = self.isCousinsHelper(root, y, 0)
        
        if depth_x > 0 and depth_y >0 and depth_x == depth_y and parent_x != parent_y:
            return True
        return False
    
    def isCousinsHelper(self, root, x, depth):
        if root == None:
            return None,  -1
        if (root.left and root.left.val == x) or (root.right and root.right.val == x):
            return root, depth + 1
        left_parent, left_depth = self.isCousinsHelper(root.left, x, depth + 1)
        if left_depth > 0:
            return left_parent, left_depth
        return self.isCousinsHelper(root.right, x, depth + 1)