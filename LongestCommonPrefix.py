# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:35:12 2019

@author: annameng
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

strs = ["aa","a"]
strs2 = ["flower","flow","flight"]
strs3 = ["dog","racecar","car"]
strs4 = ["c","acc","ccc"]

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or "" in strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        result = ""
        min_str_len = len(strs[0])
        
        for s in strs:
            if len(s) < min_str_len:
                min_str_len  = len(s)
        print(min_str_len)
        
        
        for i in range(min_str_len+1):
            result = strs[0][:i]
            for s in strs:
                if result == s[:i]:
                    continue
                else:
                    return result[:-1]
        return result
    

S = Solution()
S.longestCommonPrefix(strs) #'a'
S.longestCommonPrefix(strs2) #'fl'
S.longestCommonPrefix(strs3) #''
S.longestCommonPrefix(strs4) #''
