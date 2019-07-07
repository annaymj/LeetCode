# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:47:28 2019

@author: annayu
"""

class Solution:
    def reverse(self, x: 'int') -> 'int':
        if '-' in str(x):
            result = int('-' + (str(x)[1::])[::-1])
            return result if result > -2**31 else 0
        else:
            result = int(str(x)[::-1])
            return result if result < 2**31 else 0

S = Solution()
S.reverse(10)
S.reverse(-123)
S.reverse(1534236469)  #expect 0
        