# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:42:45 2019

@author: annameng
Given a list of words and two words word1 and word2, 
return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)
        idx1 = -1
        idx2 = -1
        
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                idx1 = i
            if word == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                result = min(result, abs(idx1 - idx2))         
    
        return result