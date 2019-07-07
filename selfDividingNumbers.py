# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:13:22 2019

@author: annayu

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.


"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = []
        
        for i in range(left, right + 1):
            if self.isDividingNumber(i):
                result.append(i)
        return result
    
    def isDividingNumber(self, num):
        list_num = list(str(num))
        if '0' in list_num:
            return False
        
        for i in list_num:
            if num%int(i) !=0:
                return False
                break
        return True
        
S = Solution()
S.selfDividingNumbers(1,22)
        
        