```
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
```

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        lmax,rmax = [0] * len(height), [0] * len(height)
        
        lmax[0] = height[0]
        for i in range(1,len(height),1):
            lmax[i] = max(height[i], lmax[i-1])
        
        rmax[-1] = height[-1]
        for j in range(len(height)-2, -1, -1):
            rmax[j] = max(height[j], rmax[j+1])
        
        ans = 0
        for i in range(1, len(height), 1):
            ans += min(lmax[i], rmax[i]) - height[i]
        
        return ans
