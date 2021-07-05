```
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
```

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp_prev = [0] * len(nums)
        dp_post = [0] * len(nums)
        dp_cnt = [0] * len(nums)
        
        # check how many consecutive 1s before this number at index i
        for i in range(1,len(nums), 1):
            if nums[i-1] == 1:
                dp_prev[i] = dp_prev[i-1] + 1
            else:
                dp_prev[i] = 0
        
        # check how many consecutive 1s after this number at index i
        for i in range(len(nums)-2,-1, -1):
            if nums[i+1] == 1:
                dp_post[i] = dp_post[i+1] + 1
            else:
                dp_post[i] = 0
        
        # add prev and post
        for i in range(len(nums)):
            dp_cnt[i] = dp_prev[i] + dp_post[i]
        
        return max(dp_cnt) + 1
      
        
       
    
    
            
        
