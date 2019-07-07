# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:41:03 2019

@author: annayu
"""

class Solution:
    def plusOne(self, digits):
        
        num = ''
        result = []
        for i in digits:
            num+=str(i)
        
        new_num = int(num) + 1
        
        for j in list(str(new_num)):
            result.append(int(j))
            
        return result

S = Solution()
S.plusOne([1,2,3])