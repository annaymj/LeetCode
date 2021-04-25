```
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:        
        index_cnt = 0
        
        for ch in t:
            if index_cnt < len(s) and ch == s[index_cnt]:
                index_cnt += 1
 
        return index_cnt == len(s)
            
        
        
        
            
        for k in dict_B.keys():
            if dict_B[k] == 1 and k not in dict_A:
                res.append(k)
        
        return res
        
        
