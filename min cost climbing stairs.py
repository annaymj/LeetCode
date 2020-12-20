```
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```
# reverse the stairs list f[i] = cost[i] + min(f[i+1],f[i+2])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        
        n = len(cost)
        dp = [0] * n
        dp[n-1] = cost[-1]
        dp[n-2] = cost[-2]
        
        for i in range(n-3,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[0],dp[1])
            
        
        
