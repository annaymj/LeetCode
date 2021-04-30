```
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 104
s consists of English letters.
```

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        s_count = Counter()
        local_max = 0
        global_max = 0
        
        # sliding window on string s:
        for i in range(len(s)):
            
            s_count[s[i]] += 1
            # check the number of unique characters
            if len(s_count.keys()) <= 2:
                local_max += 1
                global_max = max(global_max, local_max)
            else:
                if s_count[s[i-local_max]] == 1:
                    del s_count[s[i-local_max]]
                else:
                    s_count[s[i-local_max]] -= 1
                
        return global_max
                    
        
