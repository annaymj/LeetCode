# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:01:39 2019

@author: annayu
"""
from fractions import gcd

str1 = "ABCABC"
str2 = "ABC"

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        
        if set(str1) != set(str2) or l1 == 0 or l2 ==0:
            print("None")            
            #return ""        
        if l1 <= l2 and str2 == str1 * int(l2/l1):
            print("str1")
            #return str1
        if l1 > l2 and str1 == str2 * int(l1/l2):
            print("str2")
            #return str2
        
        
        n = gcd(l1,l2)
        n1 = int(l1/n)
        n2 = int(l2/n)
        
        if (str1 == str1[:n] * n1) and (str2 == str2[:n] * n2) and (str1[:n] == str2[:n]):
            return str1[:n]
        return ""
        
    def gcd(self,x,y):
        while y != 0:
            (x,y) = (y, x%y)
        return x
        
S = Solution()
S.gcdOfStrings(str1,str2)

S.gcdOfStrings("ABABAB","ABAB")
S.gcdOfStrings("LEET","CODE")