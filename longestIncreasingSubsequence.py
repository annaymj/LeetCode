# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:31:15 2019

@author: annayu
Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

subsequence does not require to be continuous

"""

nums = [10,9,2,5,3,7,101,18] #


class Solution:
    def lengthOfLIS(self, nums) -> int:
        
        # if empty
        if len(nums) == 0:
            return 0
        
        # initiate values
        dp = [1]
        ans = 1
        
        for i in range(1,len(nums),1):
            maxval = 0
            for j in range(0,i,1):
                # compare with all previous number and update the maxval
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            # update the overal maxval
            dp.append(maxval + 1)
          
        return max(dp)
        
S = Solution()
S.lengthOfLIS(nums)
        