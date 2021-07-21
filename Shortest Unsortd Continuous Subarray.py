```
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
```

from collections import deque #deque is double sided queue

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left_index = len(nums)
        right_index = 0
        stack_l = deque()
        stack_r = deque()
        
        for i in range(len(nums)):
            while(len(stack_l) != 0 and nums[stack_l[-1]] > nums[i]):
                left_index = min(left_index, stack_l.pop())
            stack_l.append(i)
        
        
        for i in range(len(nums)-1, -1, -1):
            while(len(stack_r) != 0 and nums[stack_r[-1]] < nums[i]):
                right_index = max(right_index, stack_r.pop())
            stack_r.append(i)
        
        if left_index < right_index:
            return right_index - left_index + 1
        return 0
        
    
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left_index = 0
        right_index = 0
        
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left_index = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sorted_nums[j]:
                right_index = j
                break
        
        if left_index != right_index:
            return right_index - left_index + 1
        return 0
