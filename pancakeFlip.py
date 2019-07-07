# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:33:38 2019

@author: annayu
"""

class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # result stores the number of pancakes filpped each time
        result = []
        for i in range(len(A),1,-1):
           
            # get the index of the max number in the list   
            max_index = A[:i].index(max(A[:i]))
            
            if max_index != 0:
                # flip the max to the top
                A[:max_index+1] = reversed(A[:max_index+1])
                result.append(max_index +1)
                
            # flip the max to the end
            A[:i] = reversed(A[:i])
          
            result.append(i)
        return result
         

A = [3,2,4,1]
S = Solution()
print(S.pancakeSort(A))