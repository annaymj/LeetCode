```
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


Example 2:
Input: triangle = [[-10]]
Output: -10
```

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # corner case, only 1 layer
        if len(triangle) < 2:
            return triangle[0][0]
        
        nrow = len(triangle) 
       # dp = triangle.copy() #copy triangle matrix to store the min path sum
        
        for i in range(1,nrow):
            currRow = triangle[i]
            for j in range(len(currRow)):
                # if at first and last column, there is only one choice
                if j == 0: # first column
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j == len(currRow) - 1: # last column
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j] # compare the upper and upper left min path sum
                    
        return min(triangle[nrow-1])
        
    
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        # corner case, only 1 layer
        if len(triangle) < 2:
            return triangle[0][0]
        
        nrow = len(triangle) 
        dp = triangle.copy() #copy triangle matrix to store the min path sum
        
        for i in range(1,nrow):
            currRow = triangle[i]
            for j in range(len(currRow)):
                # if at first and last column, there is only one choice
                if j == 0: # first column
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(currRow) - 1: # last column
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] # compare the upper and upper left min path sum
                    
        return min(dp[nrow-1])
        
        
