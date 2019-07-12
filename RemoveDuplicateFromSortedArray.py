# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:39:04 2019

@author: annameng
Given a sorted array nums, remove the duplicates in-place such that each element
 appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
 the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums 
being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums):
        cnt = 0
       
        while cnt < len(nums):
            cur_num = nums[cnt]
            cur_cnt = nums.count(cur_num)
            
            if cur_cnt > 1:
                for i in range(cur_cnt - 1):
                    nums.remove(cur_num)
            cnt += 1
        
        return cnt
    
    def removeDuplicates2(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i +=1
        return len(nums)
    
S = Solution()
S.removeDuplicates(nums1) 
S.removeDuplicates(nums2)  

S.removeDuplicates2(nums1) 
S.removeDuplicates2(nums2)         