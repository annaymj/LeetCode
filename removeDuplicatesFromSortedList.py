# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:14:01 2019

@author: annameng
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        prev = head
        curr = head.next
        
        if head == None:
            return head
        
        while curr != None:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next     
            else:
                prev = curr
                curr = curr.next
        
        return head
            
            