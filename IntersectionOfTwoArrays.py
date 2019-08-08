# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:58:50 2019

@author: annameng
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""
nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = set1.intersection(set2)
        
        return list(result)
        