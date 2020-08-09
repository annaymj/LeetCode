#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:37:24 2020

@author: annayu

5483. Make The String Great
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter 
but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters 
that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. 
The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

 

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, 
both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, a
nd all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
 
"""
s1 = "leEeetcode"
s2 = "abBAcC"
s3 = "s"

class Solution:
    def makeGood(self, s: str):
        if len(s) < 2:
            return s
        
        result = [s[0]]
        
        for i in range(1,len(s)):
            curr_char = s[i]
            
            if len(result) == 0:
                result.append(curr_char)
            # check if it meets the condition
            elif curr_char != result[-1] and curr_char.upper() == result[-1].upper():
                result.pop()
            else:
                result.append(curr_char)
        s_result = ''.join(result) 
        
        return s_result
        
    
S = Solution()

S.makeGood(s)
S.makeGood(s2)
S.makeGood(s3)