# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:39:12 2019

@author: annameng
coding: 找到最小的一个数，使得其 乘以 2，3，4，5 之后 和自己的digits完全一样
解释：比如【1,3,4】和【1，4，3】和【3，1，4】算是digit一样（值一样，数目一样），而【1，1，3】就不一样
"""

class Solution:
    def minNum(self):
        n = 10
        while n > 0:
            if self.sameDigit(n):
                return n
            n += 1
    
    def sameDigit(self,n):
        m = [2,3,4,5]
        boolean = []
        
        for i in m:
            n2 = n * i
            if set(str(n)) == set(str(n2)) and len(str(n)) == len(str(n2)):
                boolean.append(True)
                
        if len(boolean) == len(m):
            return True
        return False
    
S = Solution()
S.minNum()