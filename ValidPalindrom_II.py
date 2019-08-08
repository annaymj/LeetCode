# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:27:36 2019

@author: annameng
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. 
The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        if s == s[::-1]:
            return True
        
        left, right = 0, len(s) -1
        
        cnt = 0
        
        while left < right:
            
            # if the left and right char are exactly the same
            if s[left] == s[right]:
                left += 1
                right -= 1
            # the left and right are different and they are right next to each othe
            elif right - left == 1:
                return True
            
            # check if remove the left or right element, the rest are palindrom or not
            else:
                s1 = s[left:right]
                s2 = s[left+1 : right+1]
                return s1 == s1[::-1] or s2==s2[::-1]
        return True
        