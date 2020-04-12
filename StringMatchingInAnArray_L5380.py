#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:36:28 2020

@author: annayu
Given an array of string words. 
Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], 
if can be obtained removing some characters to left and/or right side of words[j].

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
"""

words1 = ["mass","as","hero","superhero"]
words2 = ["leetcode","et","code"]
words3 = ["leetcoder","leetcode","od","hamlet","am"]

class Solution:
    def stringMatching(self, words):
        result = set()
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j] in words[i] and words[j] != words[i]:
                    result.add(words[j])
                if words[i] in words[j] and words[i] != words[j]:
                    result.add(words[i])
        return list(result)
                    
S = Solution()
S.stringMatching(words1)
S.stringMatching(words2)
S.stringMatching(words3)