#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:58:54 2019

@author: annayu
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.


Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result_1 = []
        
        self.printNode(root1,result_1)
        self.printNode(root2,result_1)
        return sorted(result_1)
    
    def printNode(self,root,result):
        if root != None:
            self.printNode(root.left,result)
            result.append(root.val)
            self.printNode(root.right,result)