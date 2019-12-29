#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:34:15 2019

@author: annayu
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
"""

class Solution:
    def sumZero(self, n: int):
        result = []
        
        if n%2 == 0:
            for i in range(1,n//2 + 1):
                result.append(i)
                result.append(-1 * i)
            return result
        else:
            result.append(0)
            for i in range(1,(n-1)//2 + 1):
                result.append(i)
                result.append(-1 * i)
            return result

S = Solution()
S.sumZero(3)
S.sumZero(5)