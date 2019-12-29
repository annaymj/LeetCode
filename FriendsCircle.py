# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:25:59 2019

@author: annameng
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.
"""

class Solution:
    # method 2, bfs
    # Time complexity O(n^2), Space complexity O(n)
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [ 0 for i in range(len(M))]
        count = 0
        queue = []
        
        for i in range(len(M)):
            if visited[i] == 0:
                queue.append(i)
                while len(queue) > 0:
                    s = queue.pop(0)
                    visited[s] = 1
                    for j in range(len(M)):
                        if (M[s][j] == 1 and visited[j] == 0):
                            queue.append(j)
                count += 1
        return count
        
    
    
    # method 1, dfs, 
    # Time complexity O(n^2), Space complexity O(n)
    def findCircleNum1(self, M: List[List[int]]) -> int:
        visited = [ 0 for i in range(len(M))]
        count = 0
        
        for i in range(len(M)):
            if (visited[i] == 0):
                self.dfs(M, visited, i)
                count += 1
        return count
    
    def dfs(self,M, visited, i):
        for j in range(len(M)):
            if (M[i][j] == 1 and visited[j] == 0):
                visited[j] = 1
                self.dfs(M, visited, j)
                
                
        
        
            
          
          
        
        
        
        