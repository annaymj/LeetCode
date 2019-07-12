# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:15:00 2019

@author: annameng
iven two strings A and B of lowercase letters, 
return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        if set(A) != set(B):
            return False
        
        if A == B:
            for i in range(len(A)):
                if A.count(A[i])%2 == 0 and B.count(B[i]) %2 == 0:
                    return True
        
        diff_cnt = 0
        A_list = []
        B_list = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_cnt += 1
                A_list.append(A[i])
                B_list.append(B[i])
        
        if diff_cnt != 2 or A_list != B_list[::-1]:
            return False
        
        return True
        