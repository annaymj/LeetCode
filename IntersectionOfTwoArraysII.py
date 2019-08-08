# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:29:53 2019

@author: annameng

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

class Solution:
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1)&Counter(nums2)).elements())
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        result = []
        for num in nums1:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        
        for n in nums2:
            if n in d.keys() and d[n] > 0:
                result.append(n)
                d[n] -=1
                
        return result
            
        
        
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result_set = set1.intersection(set2)
        result = []
        
        for s in result_set:
            cnt = min(nums1.count(s), nums2.count(s))
            
            if cnt > 1:
                result.extend([s for i in range(cnt)])
            else:
                result.append(s)
        return result