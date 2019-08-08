# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:49:36 2019

@author: annameng
1137. N-th Tribonacci Number
User Accepted: 2079
User Tried: 2231
Total Accepted: 2096
Total Submissions: 3082
Difficulty: Easy
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
            
        nums = [0 for i in range(n+1)]
        nums[0] = 0
        nums[1] = 1
        nums[2] = 1
        
        for i in range(3,n+1):
            nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
        return nums[i]

S = Solution()
S.tribonacci(1)
S.tribonacci(25)   
    
    
    