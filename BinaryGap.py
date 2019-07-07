# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:24:56 2019

@author: annayu

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.
Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, 
and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        bin_N = bin(N)
        
        if bin_N.count('1') < 2:
            return 0
        
        index_list = []
        gap_list = []
        
        for i in range(len(bin_N)):
            if bin_N[i] == '1':
                index_list.append(i)
        
        # get difference between the index
        for j in range(len(index_list)-1):
            gap_list.append(index_list[j+1] - index_list[j])
        
        return max(gap_list)

S = Solution()
S.binaryGap(22)