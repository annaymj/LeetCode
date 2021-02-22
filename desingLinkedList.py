```
Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
```

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
    
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        self.size += 1
        prev  = self.head
        for _ in range(index):
            prev = prev.next 
            
        newNode = ListNode(val)      
        newNode.next = prev.next 
        prev.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        self.size -= 1
        
        prev = self.head 
        for _ in range(index):
            prev = prev.next 
        
        prev.next = prev.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
