# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:41:45 2019

@author: annameng
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        dict_n = {}
        
        for num in nums:
            if num not in dict_n.keys():
                dict_n[num] = 1
            else:
                dict_n[num] += 1
                return True
        return False