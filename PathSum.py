# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:15:37 2019

@author: annayu

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # recursion 
    # time complexity O(n), space complexity worst case O(n)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        sum -= root.val
        if root.left == None and root.right == None: # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
    # iteration
    # DFS
    def hasPathSum2(self, root, sum):
        if root == None:
            return False
            
        de = [(root, sum - root.val)]
        
        while de:
            node, curr_sum = de.pop()
            if node.left == None and node. right == None and curr_sum == 0:
                return True
            
            if node.right != None:
                de.append((node.right, curr_sum - node.right.val))
            
            if node.left != None:
                de.append((node.left, curr_sum - node.left.val))
            
       return False
        