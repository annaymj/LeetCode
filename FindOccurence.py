# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:54:50 2019

@author: annameng

"""
text = "alice is a good girl she is a good student"
first = "a"
second = "good"


text2 = "we will we will rock you"
first2 = "we"
second2 = "will"

class Solution:
    
    def findOcurrences(self, text: str, first: str, second: str):
        result = []
        
        text_list = text.split(' ')
        
        for i in range(len(text_list)-2):
                if text_list[i] == first and text_list[i+1] == second:
                    result.append(text_list[i+2])
        return result
            
S = Solution()
S.findOcurrences(text, first, second)
S.findOcurrences(text2, first2, second2)