# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:18:41 2019

@author: annayu
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "0P"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_s = ''
        for char in s:
            if char.isalpha() or char.isnumeric():
                cleaned_s += char.lower()
        return cleaned_s == cleaned_s[::-1]
        
    def isPalindrome2(self, s: str) -> bool:   
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        return s == s[::-1]

S = Solution()
S.isPalindrome(s1)
S.isPalindrome(s2)
S.isPalindrome(s3)

S.isPalindrome2(s3)