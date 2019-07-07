# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:01:40 2019

@author: annayu

703. Kth Largest Element in a Stream
Easy

299

132

Favorite

Share
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Your KthLargest class will have a constructor 
which accepts an integer k and an integer array nums, 
which contains initial elements from the stream. 
For each call to the method KthLargest.add, 
return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
"""

import bisect
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val) 
        return self.nums[-1*self.k]

class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.heap = nums[-k:]
        self.nums = sorted(nums)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if (len(self.heap) < self.k):
            heapq.heappush(self.heap,val)
        
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
            return self.heap[0]
        
        
        
        
        