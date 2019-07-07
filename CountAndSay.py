# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:04:26 2019

@author: annayu
The count-and-say sequence is the sequence of integers with 
the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        curr_num = '1'
        cnt = 1
        
        if n == 1:
            return curr_num
        
        while cnt < n:
            new_num = self.generateNext(curr_num)
            curr_num = new_num
            cnt +=1
        return curr_num
    
    def generateNext(self,curr_num):
        result = ''
        list_curr_num = list(curr_num)
        prev_num = list_curr_num[0]
        cnt = 1
        
        if len(curr_num) == 1:
            return str(cnt) + curr_num
        
        for i in range(1,len(list_curr_num)):
            num = list_curr_num[i]
            
            if num == prev_num:
                cnt += 1
            else:
                result += str(cnt) + prev_num
                cnt = 1 #reset count
                prev_num = num #update prev_num
        
        result += str(cnt) + num
        return result