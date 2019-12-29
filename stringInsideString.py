# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:50:08 2019

@author: annameng

53 occurs in 1953786 at positon 2
78 occurs in 195378678 at positons 4 and 7
57 does not occur in 153786
"""

# Given tow integers A and B, returns the leftmost positions at which A occurs in B
def solution(A,B):
    if A > B:
        return -1
    str_A = str(A)
    str_B = str(B)
    
    if str_A not in str_B:
        return -1
    return str_B.index(str_A)
    
    
    

