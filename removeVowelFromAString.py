# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:50:57 2019

@author: annameng
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, 
and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""

class Solution:
    def removeVowels(self, S: str) -> str:
        S_list = list(S)
        result = ''
        
        for s in S_list:
            if s not in ['a','e','i','o','u']:
                result += s
            
        return result