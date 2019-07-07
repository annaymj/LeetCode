# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:41:24 2018

@author: annameng
"""
test_input = [[1,1,0],[1,0,1],[0,0,0]]





def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0,len(A)):
            tmp_reverse = A[i][::-1]
            tmp_inverse = [1 - num for num in tmp_reverse]
            result.append(tmp_inverse)
        return result