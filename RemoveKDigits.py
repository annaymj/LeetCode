# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:53:43 2019

@author: annameng
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution:
    # use stack, first in last out
    # beat 62%
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        
        stack = []
        removedcount = 0
        
        for ch in num:
            while stack and ch < stack[-1] and removedcount < k:
                stack.pop()
                removedcount += 1
            stack.append(ch)
            
        for _ in range(k-removedcount):
            stack.pop()
            
        return str(int(''.join(stack)))