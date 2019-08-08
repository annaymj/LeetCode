# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:54:18 2019

@author: annameng
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        l,h = 0, len(numbers)-1
        
        while l < h:
            twoSum = numbers[l] + numbers[h]
            if twoSum == target:
                if l != h:
                    return [l+1,h+1]
            elif twoSum < target:
                l += 1
            else:
                h -= 1
        return result
        
    # hashtable is faster    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}
        result = []
        
        for i in range(1,len(numbers) + 1):
            num = numbers[i-1]
            
            if num not in d.keys():
                d[num] = i
            if target - num in d.keys():
                index1 = d[target-num]
                index2 = i
                if index1 != index2:
                    return [index1,index2]
        return result
           
            
         
                