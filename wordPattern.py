# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:20:38 2019

@author: annameng
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, 
such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, 
and str contains lowercase letters that may be separated by a single space.
"""
pattern1 = "abba"
string1 = "dog cat cat dog"

pattern2 = "abba"
string2 = "dog cat cat fish"

pattern3 = "aaaa"
string3 = "dog cat cat dog"

pattern4 = "abba"
string4 = "dog dog dog dog"


class Solution:
    # faster than 21.48%
    def wordPattern2(self, pattern: str, string: str) -> bool:
        string_list = string.split(" ")
         
        if len(pattern) == len(string_list):
            return len(set(zip(pattern,string_list))) == len(set(pattern)) == len(set(string_list))
        else:
            return False
        
    # faster than 61.22%
    def wordPattern(self, pattern: str, string: str) -> bool:
        string_list = string.split(" ")
        
        if len(pattern) != len(string_list):
            return False
        
        
        if len(set(pattern)) != len(set(string_list)):
            return False
        
        dict_p = {}
        dict_s = {}
        
        for p in pattern:
            if p not in dict_p.keys():
                dict_p[p] = 1
            else:
                dict_p[p] += 1
        
        for s in string_list:
            if s not in dict_s.keys():
                dict_s[s] = 1
            else:
                dict_s[s] += 1
       
        for i in range(len(pattern)):
            if dict_p[pattern[i]] != dict_s[string_list[i]]:
                return False
            return True
        
S = Solution()
S.wordPattern(pattern1, string1) #True
S.wordPattern(pattern2, string2) #False
S.wordPattern(pattern3, string3) #False
S.wordPattern(pattern4, string4) #False

S.wordPattern2(pattern1, string1) #True
S.wordPattern2(pattern2, string2) #False
S.wordPattern2(pattern3, string3) #False
S.wordPattern2(pattern4, string4) #False
        
        