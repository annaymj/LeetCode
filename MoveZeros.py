# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:34:16 2019

@author: annameng

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

input_s = [0,1,0,3,12]

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeros = 0
        
        for i in range(len(nums)):
            if nums[i-numZeros] == 0:
                nums.pop(i - numZeros)
                nums.append(0)
                numZeros += 1

S = Solution()
S.moveZeroes(input_s)
print(input_s)