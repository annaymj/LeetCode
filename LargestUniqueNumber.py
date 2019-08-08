# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:32:30 2019

@author: annameng
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. 
The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000
"""
import sys
class Solution:
    # faster than 69.76%
    def largestUniqueNumber(self, A: List[int]) -> int:
        A_dict = {}
        A_max = -1 * sys.maxsize
        B_dict = {}
            
        for num in A:
            if num not in A_dict.keys():
                A_dict[num] = 1
            else:
                A_dict[num] += 1
                B_dict[num] = 1
    
        for key in A_dict.keys():
            if key not in B_dict.keys():
                A_max = max(A_max,key)
                    
        return A_max if A_max != -1 * sys.maxsize else -1
            

    # faster than 6.43%
    def largestUniqueNumber2(self, A: List[int]) -> int:
        sorted_A = sorted(A,reverse = True)
        
        for num in sorted_A:
            if sorted_A.count(num) == 1:
                return num
        return -1
