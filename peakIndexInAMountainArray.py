# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:55:56 2019

@author: annameng
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that 
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, 
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1

"""

A1 = [0,1,0]  #1
A2 = [0,2,1,0] #1
A3 = [3,4,5,1] #2
A4 = [24,69,100,99,79,78,67,36,26,19] #2
A5 = [18,29,38,59,98,100,99,98,90] #5
A6 = [98,100,99,98,90] #1
class Solution:
    
    """ Linear Scan. Time :O(N); Space O(1) """
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':   
        peak_val = A[0]
        for i in range(1,len(A)):
            if A[i]> peak_val:
                peak_val = A[i]
            if A[i] <peak_val:
                return i-1
    
    def peakIndexInMountainArray2(self, A: 'List[int]') -> 'int':
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i
    """ Binary Search. Time: O(logN); Space O(1)"""
    def peakIndexInMountainArray3(self, A: 'List[int]') -> 'int':
        peak_index = int((len(A) - 1)/2)
        if A[peak_index] > A[peak_index + 1] and A[peak_index -1] < A[peak_index]:
            return peak_index
        
        elif A[peak_index -1] > A[peak_index] and A[peak_index] > A[peak_index + 1]:
            return self.peakIndexInMountainArray3(A[0:peak_index + 1])
        
        else:
            return self.peakIndexInMountainArray3(A[peak_index:len(A)]) + peak_index
        
    def peakIndexInMountainArray4(self, A: 'List[int]') -> 'int':
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = int((lo + hi)/2)
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
    
S = Solution()
S.peakIndexInMountainArray(A1)
S.peakIndexInMountainArray(A2)
S.peakIndexInMountainArray(A5)

S.peakIndexInMountainArray2(A1)
S.peakIndexInMountainArray2(A2)

S.peakIndexInMountainArray3(A1)
S.peakIndexInMountainArray3(A2)
S.peakIndexInMountainArray3(A3)
S.peakIndexInMountainArray3(A4)
S.peakIndexInMountainArray3(A5)
S.peakIndexInMountainArray3(A6)

S.peakIndexInMountainArray4(A5)