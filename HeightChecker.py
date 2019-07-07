# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:04:49 2019

@author: annayu

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  
(This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
"""
heights1 = [1,1,4,2,1,3]

class Solution:
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        
        result = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                result +=1
        return result
        
    def heightChecker2(self, heights):
        return (sum x!=y for x,y in zip(heights, sorted(heights)))

S = Solution()
S.heightChecker(heights1)