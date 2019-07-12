# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:51:44 2019

@author: annameng
"""
arr = [1,0,2,3,0,4,5,0]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_insert = 0
        for i in range(len(arr)):
            if arr[i+num_insert] == 0:
                num_insert += 1
                arr.insert(i+num_insert,0)
        
        # pop
        for i in range(num_insert):
            arr.pop()
            
S = Solution()
S.duplicateZeros(arr)
arr