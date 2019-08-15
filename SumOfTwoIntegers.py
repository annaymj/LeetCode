# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:33:37 2019

@author: annameng
bitwise operator:
a&b: if both elements are 1 then 1, else 0
a|b: if both elements are 0 then 0, else 1
a^b: if elements are the same then 0, else 1
~a: Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
This is the same as -x - 1
"""

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7fffffffffffffffffffffffffffffff # 128-bit
        mask = 0xffffffffffffffffffffffffffffffff
        
        while b:
            a, b = (a ^ b) & mask, ((a&b)<<1) & mask
            
        if a <= MAX:
            return a
        else:
            return ~(a^mask)
        
        
    def add(self, a,b):
        while b != 0:
            
            carry = a&b
            
            a = a^b
            b = carry <<1
        
        return a
        