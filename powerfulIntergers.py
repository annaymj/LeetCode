# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:39:22 2019

@author: annayu
"""

x = 2
y = 3
bound = 10


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = []
        i=0
        j=0
        currVal = x **i + y **j
        while x**i + y**j <= bound:
            result.append(currVal)
        
            while x**i + y** j <= bound:
                currVal = x**i + y** j
                result.append(currVal)
                print("i:" +str(i))
                print ("j:" + str(j))
                print("currVal:" + str(currVal))
                j +=1
                
            i +=1
            j = 0
            
        return list(set(result))
        

s = Solution()
s.powerfulIntegers(x,y,bound)