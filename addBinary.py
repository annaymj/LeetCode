# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:03:03 2019

@author: annameng

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

a = "11"
b = "1"


class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        int_a = int(a,2)
        int_b = int(b,2)
        return bin(int_a + int_b)[2:]

S = Solution()
S.addBinary(a,b)