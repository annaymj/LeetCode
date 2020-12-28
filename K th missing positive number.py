```
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```

class Solution:
    # O(logN)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            pivot = left + (right - left)//2
            if arr[pivot] - (pivot + 1) < k:
                left = pivot + 1
            else:
                right = pivot - 1
# numbers of missing numbers at arr[right] should be arr[right] - (right + 1)  
# so the number to return should be:
# arr[right] + k - (arr[right] - (right+1)) = k + right +1
        return right + k + 1
    # O(N)
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        max_len = arr[-1] + k
        num_missing = 0
        num_dict = {}
        
        for num in arr:
            num_dict[num] = 1 # since there is no duplicate
        
        for i in range(max_len):
            if i+1 not in num_dict.keys():
                num_missing +=1
            if num_missing == k:
                return i+1
            
            
            
        
