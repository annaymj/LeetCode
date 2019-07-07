# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:42:01 2019

@author: annayu
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element 
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
"""

class Solution:
    def majorityElement(self, nums):
        
        # if there is only one num, return that num
        if len(nums) == 1:
            return nums[0]
        
        set_num = set(nums)
        max_cnt = 1
        maj_num = 1
        
        for item in set_num:
            item_cnt = nums.count(item)
            
            if item_cnt > max_cnt:
                max_cnt = item_cnt
                maj_num = item
                
        return maj_num