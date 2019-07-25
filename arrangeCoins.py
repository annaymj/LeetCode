# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:04:59 2019

@author: annameng
"""
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # assume int is a positive integer
        if n == 0:
            return 0
        
        if n <=2:
            return 1
        
        result = 0
        l,h = 1,n
        
        while l < h:
            m = l + (h-l)//2
            if m*(1+m)/2 == n:
                return (m)
            if m*(1+m)/2 < n:
                l = m + 1
                result = max(result,m)
            else:
                h = m
        return result
    
    def arrangeCoins2(self, n: int) -> int:
        k = int(math.sqrt(2*n))
        
        if k*(k+1) > 2*n:
            return k-1
        return k
        
S = Solution()
S.arrangeCoins(5)   #2 
S.arrangeCoins(8)   #3

S.arrangeCoins2(5)   #2 
S.arrangeCoins2(8)   #3