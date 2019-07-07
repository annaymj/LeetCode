# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 01:57:58 2019

@author: annameng
Given a string, you need to reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


input1 = "Let's take LeetCode contest"

class Solution:
    
    """ Simple Solution. Time: O(n). Space: O(n)"""
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        s_split = s.split()
        for word in s_split:
            word_rev = word[::-1]
            result += word_rev + " "
        
        result = result.strip()
        return result
    

S = Solution()
S.reverseWords(input1)
    
    