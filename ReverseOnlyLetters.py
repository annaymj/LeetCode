# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:05:37 2019

@author: annameng
Given a string S, return the "reversed" string where all characters 
that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters= []
        non_letters_idx = []
        non_letters = []
        
        for i in range(len(S)):
            s = S[i]
            
            if s.isalpha():
                letters.insert(0,s)
            else:
                non_letters_idx.append(i)
                non_letters.append(s)
                
                
        for i in range(len(non_letters)):
            idx = non_letters_idx[i]
            char = non_letters[i]
            # insert in to letters
            letters.insert(idx,char)
            
        return ''.join(letters)