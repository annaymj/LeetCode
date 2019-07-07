# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:16:33 2018

@author: annameng

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

# in this example, we modified the output to be the element in the list

"""
import time

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i<j:
                    result.append([nums[i],nums[j]])
        return result
    
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [] 
        # if the 2 numbers are exactly the same, e.g. nums = [3,3]
        if nums.count(target/2) == 2 :
            return[target/2,target/2]
            
        nums_dict = dict(zip(nums,range(len(nums))))
        for i in range(len(nums)):
            currNum = nums[i]
            if target - currNum in nums_dict.keys() and nums_dict.get(currNum) < nums_dict.get(target-currNum):
                    result.append([currNum,target-currNum])
        return result
    
    # this is the fastest super solution
    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        dict={}
        for i in range(0,len(nums)):
            currNum=nums[i]
            if target - currNum in dict:
                result.append([currNum,target-currNum])
            # add the number value as key, number index as value in dictionary
            dict[currNum] = i
        return result
            
        
        
def main():

    S = Solution()
    nums = [2,7,11,15,1,8,4.5,4.5]
    target = 9 
    
    t0 = time.time() 
    print(S.twoSum(nums,target))
    t1 = time.time()
    total1 = t1-t0
    print(total1)
    
    t3 = time.time() 
    print(S.twoSum2(nums,target))
    t4 = time.time()
    total2 = t4-t3
    print(total2)


    print(S.twoSum3(nums,target))
   
main()
