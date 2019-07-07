# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:52:24 2019

@author: annayu

1002. Find Common Characters

Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list 
(including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
Input0 = ["bella","roller"]
Input1 = ["bella","label","roller"]
Input2 = ["cool","lock","cook"]

import collections

class Solution:
    def commonChars(self, A):
        
        str_dict = {}
        shared_char = set()
        result = []
        
        # initiate dict
        for char in A[0]:
            str_dict[char] = A[0].count(char)
            shared_char.add(char)
        
        for eachStr in A[1::]:
            newChar = set()
            for eachChar in eachStr:
                if eachChar not in str_dict.keys():
                   continue
               # if aready there , get the min count
                else:
                   str_dict[eachChar] = min(str_dict[eachChar],eachStr.count(eachChar))
                   newChar.add(eachChar)
                  
            # update shared_char
            shared_char = shared_char.intersection(newChar)
            
         # format result
        for key in str_dict.keys():
            if key in shared_char:
                for num in range(str_dict[key]):
                    result.append(key)
                                         
        return result
        
        
    def commonChars2(self, A):
        c = collections.Counter(A[0])
        for i in range(1, len(A)):
            c &= collections.Counter(A[i])
        return list(c.elements())
            
            
S =Solution()
S.commonChars(Input1)
S.commonChars(Input2)

S.commonChars2(Input1)
S.commonChars2(Input2)
        
        