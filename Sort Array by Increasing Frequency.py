```
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

```

class Solution:
    def frequencySort(self, A):
        count = collections.Counter(A)
        return sorted(A, key=lambda x: (count[x], -x))
    
    def frequencySort2(self, nums: List[int]) -> List[int]:
        # Determine the frequency of each character.
        counts = collections.Counter(nums)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets)):
            sorted_buckets = sorted(buckets[i], reverse = True)
            for c in sorted_buckets:
                string_builder.extend([c] * i)

        return string_builder
    
    
