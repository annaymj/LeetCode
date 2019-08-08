# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:49:52 2019

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
@author: annameng
"""
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx_m = 0
        idx_n = 0
        
        while idx_m < n+m and idx_n < n:
           
            num1 = nums1[idx_m]
            num2 = nums2[idx_n]
            
            if num2 > num1:
                idx_m +=1
                
            if num2 <= num1:
                # insert the number
                nums1.insert(idx_m,num2)
                idx_m += 1
                idx_n += 1
                nums1.pop()
  
        # append the rest sorted arrays
        if idx_n < n:
            k = n - idx_n
            nums1[m+n-k:m+n] = nums2[n-k:n]
            
            
S = Solution()
S.merge(nums1,m, nums2, n)
nums1
                    

    
                