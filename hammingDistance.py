# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:36:34 2019

@author: annameng

The Hamming distance between two integers is the number of positions
 at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b_x = bin(x)[2:]
        b_y = bin(y)[2:]
        
        if len(b_x) > len(b_y) :
            b_y = self.addZeros(b_y, len(b_x) - len(b_y))
        elif len(b_x) < len(b_y):
            b_x = self.addZeros(b_x, len(b_y) - len(b_x))
        
        num_diff = 0
        
        for i in range(len(b_x)):
            if b_x[::-1][i] != b_y[::-1][i]:
                num_diff += 1
                
        return num_diff
    
    def addZeros(self, x,n):
        return '0' * n + x
        

S = Solution()
S.hammingDistance(1,4) #2