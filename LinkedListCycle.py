# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:23:22 2019

@author: annayu

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list 
where tail connects to. 
If pos is -1, then there is no cycle in the linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # time complexity O(n), space complexity O(1)
    def hasCycle(self,head):
        if (head == None or head.next == None):
            return False
        
        slow = head
        fast = head.next
        
        while (slow != fast):
            if (fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
    
    # time complexity O(n), space complexity O(1)
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_dict = {}
        
        while head != None:
            if head in node_dict.keys():
                return True
            else:
                node_dict[head] = 1
            head =head.next
        
        return False