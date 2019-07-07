#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:47:38 2019

@author: annayu
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
    def singleNumber1(self, nums):
        """
        space complexity: O(n2)
        time complexity O(n)
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
    
    def singleNumber2(self, nums):
        """
        time complexity O(n)
        space complexity O(n)
        :type nums: List[int]
        :rtype: int
        """
        hash_table={}
         
        for i in nums:
           try:
            hash_table.pop(i)
           except:
            hash_table[i] = 1
        
        return hash_table.popitem()[0]
    
    def singleNumber3(self, nums):
        """
        time complexity: O(n)
        space complexity: O(n)
        :type nums: List[int]
        :rtype: int
        Concept: 2∗(a+b+c)−(a+a+b+b+c)=c
        """
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber(self,nums):
        """
        Approach 4: Bit Manipulation
        Concept

         If we take XOR of zero and some bit, it will return that bit
         a XOR 0 =a
         If we take XOR of two same bits, it will return 0
         a XOR a =0
         a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        """
        a = 0
        for i in nums:
            a ^= i
        return a
            
        
                
        