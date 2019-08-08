# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:13:18 2019

@author: annameng
Given a string s consists of upper/lower-case alphabets 
and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_s = s.split(" ")
        if len(list_s) < 1:
            return 0
        
        return len(list_s[-1])