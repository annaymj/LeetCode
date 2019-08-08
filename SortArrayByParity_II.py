# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:30:26 2019

@author: annameng
Given an array A of non-negative integers, 
half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; 
and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        result = []
        
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
                
        for i in range(len(odd)):
            result.append(even[i])
            result.append(odd[i])
        
        return result