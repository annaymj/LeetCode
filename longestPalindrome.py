# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:23:58 2019

@author: annameng

example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

example 2:
Input: "cbbd"
Output: "bb"  


"""


class Solution:
    
    # this solution has time complexity o(n^3)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        largest_len = 0
        largest_p = ""
        
        # empty string or only one unique character
        if len(set(s)) <= 1:
            return s
        else: 
            for i in range(len(s)):
                
                for j in range(i+1,len(s),1):
                    if s[i:j+1] == s[i:j+1][::-1]:
                        if largest_len < j+1-i:
                            print(i,j)
                            print(s[i:j])
                            largest_len = j+1-i
                            largest_p = s[i:j+1]
            if len(largest_p) == 0:
                largest_p = s[0]
            return largest_p
        

S = Solution()

S.longestPalindrome("babad")

S.longestPalindrome("cbbd")

S.longestPalindrome("bbb")

S.longestPalindrome("abb")

S.longestPalindrome("ac")

S.longestPalindrome("abcda")