# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:41:09 2019

@author: annayu

1005. Maximize Sum Of Array After K Negations

Given an array A of integers, we must modify the array in the following way: 
we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
"""
A = [4,2,3] #5
A2 = [3,-1,0,2] #6
A3 = [2,-3,-1,5,-4] #13
A4 = [-2,5,0,2,-2] #11
A5 = [5,6,9,-3,3] #20
A6 = [-4,-6,9,-2,2] #19

class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        A = sorted(A)
        n_negative = sum([a<0 for a in A])
        n_zero = sum([a==0 for a in A])
        
        #  replace all negative or zero
        if n_negative > K or n_negative + n_zero >= K:
            for i in range(K):
                A[i] = -A[i]
        # if there is no negative
        elif n_negative == 0 and K%2 == 1:
            A[0] = -A[0]
        # if there is zero, just change the negative
        elif n_negative != 0 and n_zero != 0:
            for i in range(n_negative):
                A[i] = -A[i]
            
        # if there is only negative and positive 
        else:
            for i in range(n_negative):
                A[i] = - A[i]
            A = sorted(A)
            if (K - n_negative)%2 == 1:
                A[0] = -A[0]
                
        return sum(A)
        
        
            

S = Solution()
S.largestSumAfterKNegations(A,1)
S.largestSumAfterKNegations(A2,3)
S.largestSumAfterKNegations(A3,2)
S.largestSumAfterKNegations(A4,3)
S.largestSumAfterKNegations(A5,2)
S.largestSumAfterKNegations(A6,4)