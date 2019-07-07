# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:54:58 2019

@author: annameng

Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""


s1 = "leetcode" 
s2 = "loveleetcode"

class Solution:
    # O(N^2)
    def firstUniqChar(self, s: 'str') -> 'int':
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
    
    # O(N)
    def firstUniqChar2(self, s: 'str') -> 'int':
        s_dict = {}
        for char in s:
            if char not in s_dict.keys():
                s_dict[char] = 1
            else:
                s_dict[char] += 1
                
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1
    
S = Solution()
S.firstUniqChar(s1)
S.firstUniqChar(s2)

S.firstUniqChar2(s1)
S.firstUniqChar2(s2)