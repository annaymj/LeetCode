# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:01:43 2019

@author: annayu

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to 
the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
 after one shift on A. 
 Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""

A1 = 'abcde'
B2 = 'cdeab'
 
A = "bbbacddceeb"
B = "ceebbbbacdd"
 
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B) or set(A) != set(B):
            return False
    
        len_A = len(A)
        index = 0
      
        for i in range(len(A)):
            # if char does not equal to the 1st char in B, add to rotate_A list
            if A[i:len_A] != B[0: len_A - i]:
                continue
            else:
                index = i
                break
        #print(index)      
        rest_A = A[index:len_A]
        rest_B = B[0: len_A-index]
        rotate_B = B[len_A-index: len_A]
        rotate_A = A[0:index]
        
        return rotate_A == rotate_B and rest_A == rest_B 

S = Solution()
S.rotateString(A,B)