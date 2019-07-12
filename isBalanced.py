# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:49:30 2019

@author: annameng
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
	    #Variable to check at each level if the tree is balanced 
        self.isBalancedFlag = True
        if not root:
            return self.isBalancedFlag
			
		#Helper function
        def dfs(root,level):
			#Depth of left and right subtrees
            lDepth = dfs(root.left,level+1) if root.left else level
            rDepth = dfs(root.right,level+1) if root.right else level
			
            if abs(lDepth-rDepth) > 1:
                self.isBalancedFlag = False
			
            return max(lDepth,rDepth)
        
        dfs(root,0)
        return self.isBalancedFlag
    
    
        
        