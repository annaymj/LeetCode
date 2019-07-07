# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 23:35:49 2019

@author: annayu

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
"""
import sys

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-2,1]
nums3 = [-2,1,2]
nums4 = [1,2]

class Solution:
    
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        # initiate max_sum with 1st element in the list
        # min_sum: for the first i numbers, the min of first 0-k numbers
        # max_sum: overall max
        # cur_sum: sum of first i numbers
        min_sum, max_sum = 0, -sys.maxsize
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum - min_sum)
            min_sum = min(min_sum, cur_sum)
        return max_sum

"""
    def maxSubArray1(self, nums: 'List[int]') -> 'int':
        # initiate max_sum with 1st element in the list
        max_sum = nums[0]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1): # include last number
                cur_sum = sum(nums[i:j])
                if cur_sum > max_sum:
                    max_sum = cur_sum
    
        return max_sum
"""        
        
    
        
        
S = Solution()
print(S.maxSubArray(nums))
print(S.maxSubArray(nums2))
print(S.maxSubArray(nums3))
print(S.maxSubArray(nums4))



max_sum = nums2[0]
for i in range(len(nums2)):
    print("i:",i)
    for j in range(i+1, len(nums2)):
        print("j:",j)       
        cur_sum = sum(nums2[i:j])
        print("cur_sum",cur_sum)
        if cur_sum > max_sum:
            max_sum = cur_sum