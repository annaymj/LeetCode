# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:32:28 2018

266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true

@author: annameng
"""

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1] or len(x)> len(set(x)):
            return True
        False
            
            