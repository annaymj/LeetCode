# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:31:05 2019

@author: annameng
"""
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import string
s = 'a b c,d'
s.replace(string.punctuation,' ')

tweet = "I am tired! I like fruit...and milk"
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
tweet.translate(translator)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_p = paragraph.lower()
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
        p = new_p.translate(translator)
        p_list = p.strip().split(' ')
        p_list.remove('')
        
        cnt={}
        for p in p_list:
            if p not in banned:
                if p not in cnt.keys():
                    cnt[p] = 1
                else:
                    cnt[p] += 1
        
        return max(cnt,key = cnt.get)
        
                