#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:09:19 2019

@author: annayu

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        
        for i in range(s_len//2):
            # swap char
            lower_c = s[i]
            higher_c = s[s_len-1-i]
            
            s[i],s[s_len-1-i] = higher_c, lower_c
        