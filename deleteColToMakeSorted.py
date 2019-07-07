# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:17:14 2019

@author: annayu
"""

A = ["cba","daf","ghi"]

class Solution:
    def minDeletionSize(self, A) -> int:
        new_A = []
        result = 0
        nrow = len(A)
        ncol = len(A[0])
        
        # add new item to new_A
        for i in range(ncol):
            new_str = ''
            for j in range(nrow):
                new_str +=A[j][i]
            new_A.append(new_str)
        
        # check whether each are sorted
        for item in new_A:
            if item !=''.join(sorted(item)):
                result += 1
        return result
        
        
    def minDeletionSize2(self, A) -> int:
        result = 0
        
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col)-1)):
                result +=1
        return result
        
S = Solution()
S.minDeletionSize(A)
S.minDeletionSize2(A)

        