# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:48:17 2018

@author: annameng
"""
import string
code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
        ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
        ".--","-..-","-.--","--.."]

def uniqueMorseRepresentations(words):
    returnList = []
    for word in words:
        returnStr = ""
        for char in word:
            returnStr += code[string.ascii_lowercase.index(char)]
        returnList.append(returnStr)
    
    returnSet = set(returnList)
    return len(returnSet)