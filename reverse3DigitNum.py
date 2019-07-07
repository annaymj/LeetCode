# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 00:39:45 2019

@author: annayu
37. Reverse 3-digit Integer


Example
Example 1:
Input: number = 123
Output: 321

Example 2:
Input: number = 900
Output: 9

Notice
You may assume the given number is larger or equal to 100 but smaller than 1000.
"""

number1 = 123
number2 = 900

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        return int(str(number)[::-1])
    
    def reverseInteger2(self, number):
        num1 = number//100
        num2 = number//10 % 10
        num3 = number % 10
        return num3 * 100 + num2 * 10 + num1
    
    
S = Solution()
S.reverseInteger(number1)
S.reverseInteger(number2)

S.reverseInteger2(number1)
S.reverseInteger(number2)