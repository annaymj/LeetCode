```
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
```
# Algorithm
#(1) When calling the enqueue method, simply push the elements into the stack 1.
#(2) If the dequeue method is called, push all the elements from stack 1 into stack 2, which reverses the order of the elements. Now pop from stack 2.

class MyQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []
        

    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()
     
    def peek(self) -> int:
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]
    
    def empty(self) -> bool:
        if not self.stackin and not self.stackout:
            return True
        return False
