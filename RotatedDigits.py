# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:31:26 2019

@author: annayu

X is a good number if after rotating each digit individually by 180 degrees,
 we get a valid number that is different from X.  
 Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 
0, 1, and 8 rotate to themselves; 
2 and 5 rotate to each other; 
6 and 9 rotate to each other, 
and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, 
since they remain unchanged after rotating.
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        for i in range(1,N+1):
            if self.isGood(i):
                result +=1
        return result
    
    def isGood(self, n):
        new_n = ''
        list_n = list(str(n))
        for i in range(len(list_n)):
            if list_n[i] in ['0','1','8']:
                new_n += list_n[i]
            elif list_n[i] == '5':
                new_n += str(2)
            elif list_n[i] == '2':
                new_n += str(5)
            elif list_n[i] == '6':
                new_n += str(9)
            elif list_n[i] == '9':
                new_n += str(6)
            else:
                return False
        if new_n != str(n):
            return True
        return False
    
    def rotatedDigits2(self, N):
        ans = 0
        # For each x in [1, N], check whether it's good
        for x in range(1, N+1):
            S = str(x)
            # Each x has only rotateable digits, and one of them
            # rotates to a different digit
            ans += (all(d not in '347' for d in S)
                    and any(d in '2569' for d in S))
        return ans