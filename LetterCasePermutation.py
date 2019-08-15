# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:57:03 2019

@author: annameng
Given a string S, we can transform every letter individually to be lowercase 
or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

class Solution:
    # time complexity O(2^N * N), space complexity O(2^N * N)
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [[]]
        
        for s in S:
            n = len(ans)
            if s.isalpha():
                # duplicate everything
                for i in range(n):
                    # make a seperate copy of the list
                    ans.append(ans[i][:])
                    ans[i].append(s.lower())
                    ans[n+i].append(s.upper())
            else:
                for i in range(n):
                    ans[i].append(s)
                    
        return map("".join, ans)
        