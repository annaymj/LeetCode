```
Two key operations: 

swim(i): check if heap[i] is smaller than its parent, and if it is, swap it with the parent ( (i-1) // 2 ), and swim(parent)

sink(i): check if heap[i] is larger than either of its children, and if it is, swap it with the lesser of the children, and sink(child)

```
class PriorityQueue:
    def __init__(self):
        self._heap = []
    
    # add an element to heap and put in the right position
    def push(self,a):
        self._heap.append(a)
        self._swim(len(self._heap)-1)
    
    # remove and return the min element
    def remove(self):
        if len(self._heap) > 0:
            # swap top with last element
            n = len(self._heap)
            self._swap(0, n-1) 
            smallest = self._heap.pop() # after swap, the last element is the smallest
            self._sink(0)
            return smallest
        return None
    
    # check if element at i is smaller than parent, swap if needed
    def _swim(self, i):
        if i > 0:
            j = (i-1)//2 
            if self._heap[i] < self._heap[j]:
                self._swap(i,j)
                self._swim(j)
    
    # check if element at i is larger than either child, swap if needed
    def _sink(self, i):
        # must find smaller of the two children
        n = len(self._heap)
        c = 2 * i + 1 # left child
        if c < n: # make sure left child exists, otherwise we are at the bottom
            # check if right child is the better candidate
            if c + 1 < n and self._heap[c+1] < self._heap[c]:
                c += 1 # choose the larger right child
            
            # see if we need to sink
            if self._heap[c] < self._heap[i]:
                self._swap(i,c)
                self._sink(c)
        
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
              
