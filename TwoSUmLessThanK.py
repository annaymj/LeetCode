#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:23:08 2020

@author: annayu
Given an array A of integers and integer K, 
return the maximum S such that there exists i < j with A[i] + A[j] = S 
and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.

Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
"""

A1 = [34,23,1,24,75,33,54,8]
K1 = 60

A2 = [10,20,30]
K2 = 15

class Solution:
    def twoSumLessThanK(self,A,K):
        A.sort()
        res = -1
        l = 0
        r = len(A) - 1
        
        while l < r:
            if A[l] + A[r] >= K:
                r-=1
            else:
                res = max(res, A[l] + A[r])
                l+=1
        return res
        
    
    
    
    
    
    def twoSumLessThanK2(self, A, K):
        s = -1
        A2 = []
        
        for a in A:
            if a < K:
                A2.append(a)
        
        for i in range(len(A2)):
            for j in range(i+1,len(A2)):
                s_sum = A2[i] + A2[j]
                if s_sum < K:
                    s = max(s,s_sum)                
        
        return s
        

S = Solution()
S.twoSumLessThanK(A1,K1)
S.twoSumLessThanK2(A1,K1)

S.twoSumLessThanK(A2,K2)
S.twoSumLessThanK2(A2,K2)