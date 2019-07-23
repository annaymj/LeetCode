# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:07:15 2019

@author: annameng

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
"""

arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]
# 13

arr1 = [1,-2,-5,0,10]
arr2 = [0,-2,-1,-7,-4]
#20

class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        n = len(arr1)
        result = 0
        for sign1 in [-1, 1]:
            for sign2 in [-1, 1]:
                b = []
                for i in range(n):
                    b.append(arr1[i] * sign1 + arr2[i] * sign2 + i)
                result = max(result, max(b) - min(b))
        return result

    # slow solution, time exceed
    def maxAbsValExpr2(self, arr1, arr2):
        max_val = 0
        arr_len = len(arr1)
        
        for i in range(arr_len-1):
            for j in range(i+1,arr_len):
                cur_max = abs(arr1[j] - arr1[i]) + abs(arr2[j] - arr2[i]) + (j-i)
                if cur_max > max_val:
                    max_val = cur_max
        return max_val
    
S = Solution()
S.maxAbsValExpr(arr1,arr2)