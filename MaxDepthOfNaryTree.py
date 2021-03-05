```
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

```

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        q = deque()
        
        if root is None:
            return 0
        else:
            q.append(root)
        
        n_level = 0
        
        while q: # keep pop left of q till empty
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                if node.children is not None:
                    for c in node.children:
                        q.append(c)
            
            n_level += 1
        
        return n_level 
        
