# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:25:06 2019

@author: annameng
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        length = len(nums)
        result = []
        
        for i in range(1,length + 1):
            if i not in nums_set:
                result.append(i)
        return result
        