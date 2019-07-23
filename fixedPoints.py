# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:24:22 2019

@author: annameng

Given an array A of distinct integers sorted in ascending order, 
return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

"""

A =  [-10,-5,0,3,7]  # 3
A2 = [ -10, -5, 2, 3, 7]  #1

class Solution:
    def fixedPoint(self, A):
        
        for i in range(len(A)):
            if i == A[i]:
                return i
        return -1
    
    # binary search
    def fixedPoint2(self, A):
        
        result = float('inf')
        
        l,h = 0,len(A)
        
        while l < h:
            
            m = l + (h-l)//2
           # print("m is" + str(m))
            
            if A[m] == m:
                h = m
                result = min(result,m)
            elif A[m] < m:
                l = m + 1
            else:
                h = m
        return result if result != float('inf') else -1
    

S = Solution()
S.fixedPoint(A2)
S.fixedPoint2(A2)