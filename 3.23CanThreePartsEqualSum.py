# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:37:59 2019

@author: annayu
"""

A = [0,2,1,-6,6,-7,9,1,2,0,1]
A2 = [0,2,1,-6,6,7,9,-1,2,0,1]
A3 = [3,3,6,5,-2,2,5,1,-9,4]
A4 = [18,12,-18,18,-19,-1,10,10]
A5 = [14,24,-14,-20,-3,14,27,-15,1,14]
A6 = [15,20,-6,-17,-9,1,20,-1,13]
A7 = [2,8,15,-5,0,9,-3,4]


class Solution:
    
    # time limit exceeded
    def canThreePartsEqualSum(self, A) -> bool:
        
        for i in range(1,len(A),1):
            sum1 = sum(A[0:i])
            
            for j in range(i,len(A),1):
                sum2 = sum(A[i:j])
                
                if sum2 == sum1 and sum(A[j:len(A)]) == sum1:
                    print(i,j)
                    return True
        return False
        
    def canThreePartsEqualSum2(self, A) -> bool:
        
        if len(A) < 3:
            return False
        
        elif sum(A[0:len(A)-2]) == A[-2] == A[-1]:
            return True
        
        elif A[0] == sum(A[1:len(A)-1]) == A[-1]:
            return True
        
        elif A[0] == A[1] == sum(A[2:len(A)]):
            return True
        
        for i in range(1,len(A),1):
            sum1 = sum(A[0:i])
            if (sum1) > sum(A)/3:
                continue
            
            for j in range(i,len(A),1):
                sum2 = sum(A[i:j])
                if sum2 > sum(A[i::])/2:
                    continue
                
                if sum2 == sum1 and sum(A[j:len(A)]) == sum1:
                    return True
        return False
        
    def canThreePartsEqualSum3(self, A) -> bool:
        
        if len(A) < 3:
            return False
        elif sum(A)%3 != 0:
            return False
        else:
            
            parts_sum = sum(A)/3
            cur_sum = 0
            cnt = 0
            for i in range(len(A)):
                cur_sum += A[i]
                if cur_sum == parts_sum and cnt != 2:
                    cur_sum = 0 # reset cur_sum
                    cnt += 1
            return cnt == 2 and cur_sum == parts_sum
        

                
S = Solution()
S.canThreePartsEqualSum(A)
S.canThreePartsEqualSum(A2)
S.canThreePartsEqualSum(A3)
S.canThreePartsEqualSum(A4)
S.canThreePartsEqualSum(A5)
S.canThreePartsEqualSum(A6)
S.canThreePartsEqualSum3(A7)

S.canThreePartsEqualSum2(A)
S.canThreePartsEqualSum2(A2)
S.canThreePartsEqualSum2(A3)
S.canThreePartsEqualSum2(A4)
S.canThreePartsEqualSum2(A5)
S.canThreePartsEqualSum2(A6)
S.canThreePartsEqualSum2(A7)

S.canThreePartsEqualSum3(A)