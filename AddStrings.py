# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:32:47 2019

@author: annameng
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

num1 = "1"
num2 = "8"

num1_2 = "10"
num2_2 = "100"

num1_3 = "0"
num2_3 = "0"

num1_4 = "-25"
num2_4 = "2"


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        
        num1_int = self.strToInt2(num1) if "-" not in num1 else -1 * self.strToInt2(num1[1::])
        num2_int = self.strToInt2(num2) if "-" not in num2 else -1 * self.strToInt2(num2[1::])
        
        result_int = num1_int + num2_int
        return str(result_int)
    
    def strToInt(self, num):
        num_list = list(num)
        num_int = 0
        num_list = num_list[::-1]
        for i in range(len(num_list)):
            if num_list[i] == "1":
                num_int += 1 * (10 ** i)
            elif num_list[i] == "2":
                num_int += 2 * (10 ** i)
            elif num_list[i] == "3":
                num_int += 3 * (10 ** i)
            elif num_list[i] == "4":
                num_int += 4 * (10 ** i)
            elif num_list[i] == "5":
                num_int += 5 * (10 ** i)
            elif num_list[i] == "6":
                num_int += 6 * (10 ** i)
            elif num_list[i] == "7":
                num_int += 7 * (10 ** i)
            elif num_list[i] == "8":
                num_int += 8 * (10 ** i)
            elif num_list[i] == "9":
                num_int += 9 * (10 ** i)      
            else:
                num_int  = num_int  # in case of 0
        return num_int
    
    def strToInt2(self, num):
        num_list = list(num)
        num_int = 0
        num_list = num_list[::-1]
        for i in range(len(num_list)):
            digit = ord(num_list[i]) - 48
            num_int += digit * (10 ** i)
        return num_int
        
S = Solution()
S.strToInt(list(num2_2))
S.addStrings(num1,num2)
S.addStrings(num1_2,num2_2)
S.addStrings(num1_3,num2_3)
S.addStrings(num1_4,num2_4)
        