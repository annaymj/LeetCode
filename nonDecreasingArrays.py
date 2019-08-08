# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:51:11 2019

@author: annameng
Given an array with n integers, your task is to check if it could become
 non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds 
for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
nums1 = [4,2,3]
nums2 = [4,2,1]
nums3 = [3,4,2,3]
nums4 = [-1,4,2,3]
nums5 = [2,3,3,2,4]

class Solution:
    def checkPossibility(self, nums):
        # let p be the index of the index where non-ascending happens
        p = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
                #in this case, only 1 num need to be modified
        return (p is None or p == 0 or p == len(nums) - 2
                
                # make nums[p] between nums[p-1] ans nums[p+1]  
               or nums[p-1] <= nums[p+1]
                
                # make nums[p+1] between nums[p] and nums[p+2]
                or nums[p] <= nums[p+2])
            
    
S = Solution()
S.checkPossibility(nums1) #True
S.checkPossibility(nums2) #False
S.checkPossibility(nums3) #False
S.checkPossibility(nums4)
   