# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:19:00 2019

@author: annameng
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_left  = ['(','[','{']
        list_right = [')',']','}']
            
        if len(s)%2 != 0:
            print("stop 1")
            return False
            
        while i < len(s)/2:
            
            if list_left[i] in s and list_right[i] not in s:
                print("stop 2")
                return False
            elif s.index(list_left[i]) > s.index(list_right[i]):
                print("stop 3")
                return False
            elif (s.index(list_right[i]) - s.index(list_left[i])) %2 ==0:
                print("stop 4")  
                return False
            else:
                return True
            
S = Solution()
S.isValid("()")
S.isValid("()[]{}")
S.isValid("(]")
S.isValid("([)]")
S.isValid("{[]}")

Wrong! Need to use stack. Study stack vs Queue vs PriorityQueue