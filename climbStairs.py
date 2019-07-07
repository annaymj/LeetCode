# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:15:30 2019

@author: annayu
ou are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        steps.append(1)
        steps.append(1)
        
        for i in range(2, n+1):
            steps.append(steps[i-1] + steps[i-2])
            
        return steps[n]
    
    def climbStairs2(self, n: int) -> int:
        steps = [0 for x in range(n+1)]
        steps[0] = 1
        steps[1] = 1
        
        for i in range(2, n+1):
            steps[i] = steps[i-1] + steps[i-2]
            
        return steps[n]
