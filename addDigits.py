# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:11:06 2019

@author: annayu
Given a non-negative integer num, 
repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        list_num = list(str(num))
        sum_num = 0
        for i in range(len(list_num)):
            sum_num += int(list_num[i])
        
        if sum_num < 10:
            return sum_num
    
    # Digital Roots from wiki
    def addDigits2(self,num):
        return 1 + (num-1)%9
            
