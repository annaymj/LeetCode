# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:36:18 2019

@author: annameng
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_cnt = 0
        
        for s in word:
            if s == s.upper():
                cap_cnt += 1
                
        if cap_cnt == len(word):
            return True
        if cap_cnt == 0:
            return True
        if cap_cnt == 1 and word[0] == word[0].upper():
            return True
        return False