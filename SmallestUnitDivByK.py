# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:32:35 2019

@author: annayu
Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

Example 1:
Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:
Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:
Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
"""

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2 == 0  or K == 0:
            return -1
        value = 0, length = 0
        for i in range(1e6):
            value = (10 * value + 1) % K
            length += 1
            
            if (value == 0):
                return length
        return -1
            
            
            
S = Solution()
S.smallestRepunitDivByK(1)
S.smallestRepunitDivByK(2)
S.smallestRepunitDivByK(3)
S.smallestRepunitDivByK(7)
S.smallestRepunitDivByK(11)
S.smallestRepunitDivByK(13)