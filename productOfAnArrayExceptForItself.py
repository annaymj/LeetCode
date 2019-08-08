# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:47:43 2019

@author: annameng
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

"""
nums = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        left, right, result = [1]* length, [1]*length, [1]*length
        
        # construct left list
        for i in range(1,length):
            left[i] = left[i-1] * nums[i-1]
            
       # print(left)
        
        for j in range(length-2,-1,-1):
            right[j] = right[j+1] * nums[j+1]
       # print(right)
            
        for i in range(length):
            result[i] = left[i] * right[i]
            
        return result
        
            