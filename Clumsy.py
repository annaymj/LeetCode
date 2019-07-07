# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:34:39 2019

@author: annayu
1006. Clumsy Factorial

Difficulty: Medium
Normally, the factorial of a positive integer n is the product of all positive 
integers less than or equal to n.  
For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order,
 we swap out the multiply operations for a fixed rotation of operations: 
 multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  
However, these operations are still applied using the usual order of operations 
of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, 
and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  
This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, 
it returns the clumsy factorial of N.

Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

Example 2:
Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
"""




class Solution:
    def clumsy(self, N: int) -> int:
        operation = ['*','//','+','-']
        n = N-1
        cur_operation = operation * (n//4) + operation[0:n%4]
        cur_operation += ' ' #last item has no operation behind it
        result_str = ''
        
        for i in range(N):
            result_str += str(N-i) + cur_operation[i]
        print(result_str)
        return eval(result_str)
        
S = Solution()
S.clumsy(4)     
S.clumsy(10)
S.clumsy(5)
