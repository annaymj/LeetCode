# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:33:06 2019

@author: annameng
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if (head == None):
            return None
        
        if (head.val == val and head.next == None):
            return None
        
        # case when the head's val equals val
        while (head.val == val):
            if head.next == None:
                return None
            head = head.next
            
        curr = head
        prev = head
        
        while (curr != None):           
            if (curr.val != val):
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        
        return head
                
                
        