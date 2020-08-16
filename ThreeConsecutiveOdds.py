#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:53:46 2020

@author: annayu

1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive 
odd numbers in the array. Otherwise, return false.
 

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        cnt = 0
        for num in arr:
            if num%2 == 1:
                cnt += 1
                if cnt >=3:
                    return True
            else:
                cnt = 0    
        return False
        