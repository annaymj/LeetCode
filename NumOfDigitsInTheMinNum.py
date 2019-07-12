#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 23:08:57 2019

@author: annayu

Given an array A of positive integers, 
let S be the sum of the digits of the minimal element of A.

Return 0 if S is odd, otherwise return 1.

 

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, 
so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, 
and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
"""

A = [99,77,33,66,55]

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_A = list(str(min(A)))
        result = 0
        for num in min_A:
            result += int(num)
        if result % 2 == 0:
            return 1
        return 0
    
    def sumOfDigits2(self,A):
        return 0 if sum(map(int, str(min(A)))) % 2 else 1
    
    def sumOfDigits3(self,A):
        return 0 if sum([int(x) for x in str(min(A))]) % 2 else 1
    
S = Solution()
S.sumOfDigits(A)
S.sumOfDigits2(A)
S.sumOfDigits3(A)
    