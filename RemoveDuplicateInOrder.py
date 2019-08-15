# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:34:33 2019

@author: annameng
input = [4,4,3,6,6,7,7,7]，output = [4,3,6,7]
"""
input1 = [4,4,3,6,6,7,7,7]

def removeDuplicate_inOrder(nums):
    dict_n = {}
    
    for num in nums:
        if num not in dict_n.keys():
            dict_n[num] = 1
        else:
            dict_n[num] += 1
    
    return list(dict_n.keys())

removeDuplicate_inOrder(input1)