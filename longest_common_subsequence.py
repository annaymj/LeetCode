```
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # make a grid of 0's with len(text2) + 1 columns and len(text1) + 1 rows
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dp_grid[row][col] = dp_grid[row+1][col+1] + 1
                else:
                    dp_grid[row][col] = max(dp_grid[row+1][col], dp_grid[row][col+1])
        return dp_grid[0][0]
        
                
                
            
