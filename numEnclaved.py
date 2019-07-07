# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:59:44 2019

@author: annayu
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, 
or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary 
of the grid in any number of moves.

e.g 1
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

e.g 2
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
"""

A1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

def numEnclaves(A):
    m, n = len(A), len(A[0])
    
    for j in range(n):
        dfs(A,0,j)
        dfs(A,m-1,j)
        
    for i in range(m):
        dfs(A,i,0)
        dfs(A,i,n-1)
    return sum(val == 1 for row in A for val in row)
    
def dfs(A,r,c):
    if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == 1:
        A[r][c] = 0
        for newr, newc in (r-1, c), (r+1,c), (r,c-1), (r, c+1):
            dfs(A, newr, newc)
    