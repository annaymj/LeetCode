```
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
```

class UnionFind(object):
    def __init__(self):
        self._id = [i for i in range(1001)] #store the root node for a given node
        self._size = [0] * 1001
    
    # find the root node of x
    def find(self,x):
        # follow the “parent” link until the set ID is equal to element ID
        while self._id[x] != x:
            self._id[x] = self._id[self._id[x]]
            x = self._id[x]
        return x

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        
        if x_set == y_set:
            return False
        else:
            if self._size[x_set] > self._size[y_set]:
                x_set, y_set = y_set, x_set
            self._id[x_set] = y_set
            self._size[x_set] += self._size[y_set]
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for edge in edges:
            if uf.union(edge[0],edge[1]) == False:
                return edge
         
