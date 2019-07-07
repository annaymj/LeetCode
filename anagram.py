# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:09:34 2018

@author: annameng

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""

s = "anagram"
t = "nagaram"



class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set = set(s)
        t_set = set(t)
        
        if s_set != t_set:
            return False
        else:
            elem_list = list(s_set)
            for i in elem_list:
                if s.count(i) != t.count(i):
                    return False
        return True
            
test = Solution()
test.isAnagram(s,t)

# solution 2
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
