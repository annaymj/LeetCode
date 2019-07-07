# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:37:30 2019

@author: annameng

Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
A = [3,1,2,4]

class Solution:
    """ 2 passes. Time O(N), Space O(N) """
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        even = []
        odd = []
        
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
    
    def sortArrayByParity2(self, A: 'List[int]') -> 'List[int]':
        return ([x for x in A if x%2 == 0] + [x for x in A if x%2 != 0])
    


S = Solution()
S.sortArrayByParity(A)
S.sortArrayByParity2(A)