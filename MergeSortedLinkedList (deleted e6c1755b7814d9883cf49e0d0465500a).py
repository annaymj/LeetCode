# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:07:43 2019

@author: annayu
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

l1 = [1,2,4]
l2 = [1,3,4]
Result = [1,1,2,3,4,4]

# create linked list firest

 # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists1(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':  
        """Recursion """
        # Time: O(n + m), Space: O(n+m)
        if l1 is None:
            return l2        
        elif l2 is None:
            return l1        
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
        
    def mergeTwoLists2(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode': 
        """Iteration"""
        # Time: O(n+m), Space: O(1)
        prehead = ListNode(-1)
        
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
            # left over sorted list
        prev.next = l1 if l1 is not None else l2
        return prehead.next

S = Solution()
S.mergeTwoLists1(l1,l2)