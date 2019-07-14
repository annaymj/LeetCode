#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:44:51 2019

@author: annayu
1122. Relative Sort Array
User Accepted: 2732
User Tried: 2803
Total Accepted: 2789
Total Submissions: 4135
Difficulty: Easy
Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 
are the same as in arr2.  
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


"""
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]


class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []
        index_used = []
        
        for num in arr2:
            num_index = [ i for i, x in enumerate(arr1) if x == num]
            index_used += num_index
            result += [num] * len(num_index)
            
        index_unused = set(list(range(len(arr1)))) - set(index_used)
        
       
        rest = [arr1[i] for i in index_unused]
        
        result += sorted(rest)
        return result
  

S = Solution()
S.relativeSortArray(arr1,arr2)
       
        
        
            
  