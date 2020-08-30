#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:38:23 2020

@author: annayu
1566. Detect Pattern of Length M Repeated K or More Times

Example 1:
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times.
 Notice that pattern can be repeated k or more times but not less.

Example 2:
Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. 
Another valid pattern (2,1) is also repeated 2 times.

Example 3:
Input: arr = [1,2,1,2,1,3], m = 2, k = 3
Output: false
Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times. 
There is no pattern of length 2 that is repeated 3 or more times.

Example 4:
Input: arr = [1,2,3,1,2], m = 2, k = 2
Output: false
Explanation: Notice that the pattern (1,2) exists twice but not consecutively, so it doesn't count.

Example 5:
Input: arr = [2,2,2,2], m = 2, k = 3
Output: false
Explanation: The only pattern of length 2 is (2,2) however it's repeated only twice. 
Notice that we do not count overlapping repetitions.
"""
arr = [1,2,4,4,4,4]
m = 1
k = 3

arr2 = [1,2,1,2,1,1,1,3]
m2 = 2
k2 = 2

arr3 = [1,2,1,2,1,3]
m3 = 2
k3 = 3

def containsPattern(arr, m, k):
        if m*k > len(arr):
            return False
        
        for i in range(0, len(arr) - m*k + 1):
            if arr[i:i + m*k] == arr[i:i + m] * k:
                return True
        return False

containsPattern(arr,m,k)
containsPattern(arr2,m2,k2)
containsPattern(arr3,m3,k3)
containsPattern(arr,m,k)
containsPattern(arr,m,k)