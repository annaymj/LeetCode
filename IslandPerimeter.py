#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:55:54 2019

@author: annayu

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

grid2=[[1]]

grid3 = [[1,0]]

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        p=[]
        nrow = len(grid)
        ncol = len(grid[0])
        
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # if 1st row or last row
                    if i == 0:
                        result += 1
                        p.append([i,j])
                        print("border row")
                        
                    if i == nrow-1:
                        result += 1
                        p.append([i,j])
                        print("border row")
                        
                    # if 1st col or last col
                    if j == 0:
                        result += 1
                        p.append([i,j])
                        print("border col")
                        
                    if j == ncol-1:
                        result += 1
                        p.append([i,j])
                        print("border col")
                        
                    # check upper 
                    if i > 0 and grid[i-1][j] == 0:
                        result += 1
                        p.append([i,j])
                        print("upper")
                    # check left 
                    if j > 0 and grid[i][j-1] == 0:
                        result += 1
                        p.append([i,j])
                        print("left")
                    # check below
                    if i+1 < nrow and grid[i+1][j] == 0:
                        result += 1
                        p.append([i,j])
                        print("below")
                    # check right
                    if j+1 < ncol and grid[i][j+1] == 0:
                        result += 1
                        p.append([i,j])
                        print("right")
        return p, len(p)
    
S = Solution()
S.islandPerimeter(grid)
S.islandPerimeter(grid2)
S.islandPerimeter(grid3)
                        