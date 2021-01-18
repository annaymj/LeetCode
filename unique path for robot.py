```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there? 

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
```
import math

class Solution:
    # the robot has to move m-1 steps down and n-1 steps right
    # the total steps the robot need to move is (m-1) + (n-1)
    # the total steps moving down and right is abs((m-1) + (n-1)), let's call it total_steps
    # the robot has to move (m-1) steps right, let's call it right_steps,
    # so we have transformed this into a math problem : Among the total_steps, how many combination exist to have the exact right_steps?
    def uniquePaths_math(self, m: int, n: int) -> int:
        total_steps = (m-1) + (n-1)
        right_steps = m-1
        down_steps = n-1
        result = math.factorial(total_steps)/(math.factorial(right_steps) * math.factorial(down_steps))
        return int(result)
    
    # DP
    def uniquePaths_dp(self,m,n):
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
