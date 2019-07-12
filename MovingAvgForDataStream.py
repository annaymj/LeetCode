#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:50:19 2019

@author: annayu
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.num = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """   
        self.num.append(val)
      
        if len(self.num) <= self.size:
            return float(sum(self.num))/float(len(self.num))
        else:
            return float(sum(self.num[-self.size:]))/self.size
        


from collections import deque
class MovingAverage2:
    def __init__(self, size):
        self.size = size
        self.q = deque()
        self.total = 0

    def next(self, val):
        self.q.append(val)
        remove_val = 0 if len(self.q) <= self.size else self.q.popleft()
        self.total += val - remove_val
        return float(self.total) / len(self.q)