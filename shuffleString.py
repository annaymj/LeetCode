#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:51:09 2020

@author: annayu

5472. Shuffle String

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith 
position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Example 3:
Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"

Example 4:
Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"

Example 5:
Input: s = "art", indices = [1,0,2]
Output: "rat"
"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['' for _ in range(len(s))]
        for i in range(len(s)):
            index = indices[i]
            char = s[i]
            result[index] = char
        result_s = ''.join(result)
        return result_s
        
