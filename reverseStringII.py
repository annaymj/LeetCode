# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:49:37 2019

@author: annameng
Given a string and an integer k, you need to reverse the first k characters 
for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""
s = "abcdefg"
k = 2


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        q = len(s)//(2*k)
        r = len(s)%(2*k)
        result = ''
        
        for i in range(q):
            cur_s = s[i*2*k : (i+1)*2*k]
            # reverse the first k elements
            result += cur_s[0:k][::-1]
            # add the second k elemenmts
            result += cur_s[k:2*k]
        
        r_s = s[len(s) - r: len(s)]
        if r < k:
            result += r_s[::-1]
            
        if r >= k and r < 2*k:
            result += r_s[:k][::-1] + r_s[k:r]
        
        return result

S = Solution()
S.reverseStr(s,k)
            
    