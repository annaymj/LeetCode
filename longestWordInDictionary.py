# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:32:45 2019

@author: annameng
"""
words1 = ["w","wo","wor","worl", "world"]
words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words3 = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast",
          "l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]

words = words1

class Solution:
    def longestWord(self, words):
        ans = ''
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word
        return ans

S = Solution()
S.longestWord(words1)
S.longestWord(words2)