# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:36:37 2019

@author: annameng
Given an arbitrary ransom note string and another string containing letters 
from all the magazines, write a function that will return true 
if the ransom note can be constructed from the magazines ;
 otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"

class Solution:
    
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        c1 = {i:ransomNote.count(i)for i in set(ransomNote)}
        c2 = {i:magazine.count(i)for i in set(magazine)}
        
        for i in c1:
            if i not in c2:
                return False
            
            if c1[i]>c2[i]:
                return False
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        if set(ransomNote).issubset(set(magazine)) == False:
            return False
       
        r_dict = {}
        m_dict = {}
        
        for s in magazine:
            if s not in m_dict.keys():
                m_dict[s] = 1
            else:
                m_dict[s] += 1
        
        for s in ransomNote:
            if s not in r_dict.keys():
                r_dict[s] = 1
            else:
                r_dict[s] += 1
        
        for key in r_dict.keys():
            if key not in m_dict.keys():
                return False
            if r_dict[key] > m_dict[key]:
                return False
        return True
        