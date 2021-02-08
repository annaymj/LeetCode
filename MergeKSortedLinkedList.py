```
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur = head = ListNode(0)
        pq = []
        for l in lists:
            while l is not None:
                heapq.heappush(pq, l.val)
                l = l.next
        
        while len(pq) != 0:
            val = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            
        return head.next
    
    # store sorted val in a res list, then convert to LinkedList
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        res = []
      
        pq = []
        for l in lists:
            while l is not None:
                heapq.heappush(pq, l.val)
                l = l.next
        
        while len(pq) != 0:
            smallest = heapq.heappop(pq)
            res.append(smallest)
        
        # convert array into linkedList
        cur = dummy = ListNode(0)
        for n in res:
            cur.next = ListNode(n)
            cur = cur.next
        
        return dummy.next
          
        
        
                
        
