# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:06:23 2019

@author: annameng
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:
    # faster than 16.52%
    def rotate2(self, nums: List[int], k: int) -> None:
        
        for i in range(k):
            num = nums.pop()
            nums.insert(0,num)
        
    # faster than 51.53%
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] =  nums[length-k:length] + nums[0:length - k]
        