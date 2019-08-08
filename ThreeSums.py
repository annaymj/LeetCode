# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:05:50 2019

@author: annameng
Given an array nums of n integers, are there elements a, b, c in nums
 such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

It seems like you can use elements twice only if in different triplet
"""
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [1,2,-1]
nums3 = [0,0,0,0]
nums4 = [1,2,-2,-1]
nums5 = [-1,0,1,0]
nums6 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums.sort()
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, length - 1, -nums[i], results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    
        
    
    
    
    # time exceeded    
    def threeSum2(self, nums):
        if len(nums) < 3:
            return []
        
        result = []
        d = {}
        
        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        
        for i in range(len(nums)-2):
            num1 = nums[i]
            target = -1 * num1
            d[num1] -= 1
            print("i: " + str(i) + "value: " + str(num1))
                    
            for j in range(i+1, len(nums)):  
                num2 = nums[j]
                d[num2] -=1
                print("j: " + str(j) + "value: " + str(num2))
                print("target - num2: " + str(target - num2))
                
                if target - num2 in d.keys() and d[target-num2] > 0:
                    print(num1,num2,target-num2)
                    triplet = sorted([num1, num2, target- num2])
                    if triplet not in result:
                        result.append(triplet)
                
                d[num2] += 1
            d[num1] += 1  
        return result
    
    
    def threeSum_allElementOnce(self, nums):
        if len(nums) < 3:
            return []
        
        result = []
        d = {}
        
        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        
        for i in range(len(nums)-2):
            num1 = nums[i]
            target = -1 * num1
            d[num1] -= 1
            print("i: " + str(i) + "value: " + str(num1))
                    
            for j in range(i+1, len(nums)):  
                num2 = nums[j]
                d[num2] -=1
                print("j: " + str(j) + "value: " + str(num2))
                print("target - num2: " + str(target - num2))
                
                if target - num2 in d.keys() and d[target-num2] > 0:
                    print(num1,num2,target-num2)
                    triplet = sorted([num1, num2, target- num2])
                    if triplet not in result:
                        result.append(triplet)
                        d[num1] -=1
                        d[num2] -= 1
                        d[target - num2] -=1
                        
                d[num2] += 1
            d[num1] += 1
            
        return result
    
S = Solution()
S.threeSum(nums1)   # [[-1, 0, 1], [-1, -1, 2]]
S.threeSum(nums2)   # []
S.threeSum(nums3)   # [[0, 0, 0]]
S.threeSum(nums4)   # []
S.threeSum(nums5)   # [[-1, 0, 1]]
S.threeSum(nums6)   # [[-4, 1, 3], [-4, 0, 4], [-2, 1, 1], [-2, -2, 4], [-5, 1, 4], [0, 0, 0]]

                    
        