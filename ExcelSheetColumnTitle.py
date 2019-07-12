# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:54:10 2019

@author: annameng
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"  
"""
import string

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        if n <=25:
            return string.ascii_uppercase[n-1]
        
        while n > 26:
            result = string.ascii_uppercase[(n%26)-1] + result
            if n%26 == 0:
                n = n//26 -1
            else:
                n = n//26
        
        result = string.ascii_uppercase[n-1] + result
        return result
    

S = Solution()
S.convertToTitle(1) #'A'
S.convertToTitle(26) #'Z'
S.convertToTitle(27) #'AA'
S.convertToTitle(28) #'AB'
S.convertToTitle(29) #'AC'
S.convertToTitle(52) #'AZ'
S.convertToTitle(701) #'ZY'
S.convertToTitle(703) #'AAA'

        