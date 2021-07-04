```
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
```

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        
        for char in s:
            if char not in char_dict.keys():
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
        return -1
