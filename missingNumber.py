# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:23:00 2019

@author: annameng
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity.
 Could you implement it using only constant extra space complexity?
"""
class Solution:
    
    # faster than 65.29%, Time complexity O(n), space complexity O(n)
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        
        for number in range(n):
            if number not in num_set:
                return number
        
        
        
        
    # faster than 34% , time complexity o(n), space complexity O(n)
    def missingNumber2(self, nums: List[int]) -> int:
        length = len(nums)
        dict_n = {}
        for i in range(length+1):
            dict_n[i] = 1
        
        for num in nums:
            del dict_n[num]
            
        return list(dict_n.keys())[0]
            
        
