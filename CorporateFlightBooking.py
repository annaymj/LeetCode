#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:23:13 2019

@author: annayu
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] 
means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked 
on each flight in order of their label.

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
"""

bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5

class Solution:
    def corpFlightBookings(self, bookings, n):
        a = [0] * n
        for i, j, k in bookings:
            a[i - 1] += k
            if j < n:
                a[j] -= k
        seats = 0
        for i in range(n):
            seats += a[i]
            a[i] = seats
        return a
    
    # this solution cannot pass time complexity test. Max processing time exceeded
    def corpFlightBookings2(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        result = [ 0 for _ in range(n)]
            
        for booking in bookings:
            result[booking[0]:booking[1]] 
            first = booking[0]
            last = booking[1]
            num = booking[2]
            
            for i in range(first, last+1):
                result[i] += num
                
        return list(result.values())
    
S = Solution()
S.corpFlightBookings(bookings,n)