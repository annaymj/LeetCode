```
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

Example 1:
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]

Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
 

Constraints:
m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
```

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [[ 0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
        
        for m in range(len(mat1)):
            for n in range(len(mat2[0])):
                curr_sum = 0
                for k in range(len(mat1[0])):
                    curr_sum += mat1[m][k] * mat2[k][n]
                # write to res
                res[m][n] = curr_sum
        
        return res
                
