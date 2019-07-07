# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 01:09:34 2019

@author: annameng
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
"""

n1 = 1
n2 = 16
n3 = 218

class Solution:
    def isPowerOfTwo(self, n: int):
        if n == 1:
            return True
        elif n%2 !=0:
            return False
        else:
            return self.isPowerOfTwo(n/2)

S = Solution()

S.isPowerOfTwo(n1)
S.isPowerOfTwo(n2)
S.isPowerOfTwo(n3)
        
