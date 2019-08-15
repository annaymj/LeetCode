# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:40:05 2019

@author: annameng
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

class Solution:
    def findShortestSubArray(self,nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i
            right[x] = i
            count[x] = count.get(x,0) + 1 #if count does not have x, return 0
        
        ans = len(nums)
        degree = max(count.values())
    
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans
    
    def findShortestSubArray2(self, nums: List[int]) -> int:
        dict_n = {}
        max_freq = 1
        min_len = len(nums)
       
        
        for i in range(len(nums)):
            num = nums[i]
            if num not in dict_n.keys():
                dict_n[num] = [i]
            else:
                dict_n[num].append(i)
                max_freq = max(max_freq,len(dict_n[num]))
       
        for n in dict_n.keys():
            value = dict_n[n]
            if len(value) == max_freq:
                min_len = min(min_len,value[-1] - value[0] + 1)
        
        return min_len
        
            
                
        
        
            
                
        