# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:43:18 2019

@author: annayu
"""

c1 = [1,0,1,2,1,1,7,5]
g1 = [0,1,0,1,0,1,0,1]
X1 = 3


c2 = [1]
g2 = [0]
X2 = 1

c3 = [10,1,7]
g3 = [0,0,0]
X3 = 2

c4 = [2,6,3,4,8,9]
g4 = [0,0,0,1,1,0]
X4 = 4

c5  = [7,8,8,6]
g5 = [0,1,0,1]
X5= 3


c6 = [5,8]
g6 = [0,1]
X6 = 1

c7 = [2,6,6,9]
g7 = [0,0,1,1]
X7 = 1


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3

class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        
        if X >= len(grumpy):
            return sum(customers)
        
        if sum(grumpy) == 1 and X >=1:
            return sum(customers)
        
        grumpy_index = 0
        num_customer = len(customers)
        base_score = 0
        
        # calculate base satisfaction score
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base_score += customers[i]
        max_score = base_score
        
        for i in range(grumpy_index, num_customer - X + 1):
            cur_score = base_score
            print("Staring base score:" + str(cur_score))
            # check if there is any grumpy
            if sum(grumpy[i:i + X]) == 0:
                continue
            else:
                for j in range(X):           
                    if grumpy[i + j] == 1:
                        print("i+j is", str(i+j))
                        cur_score += customers[i+j]
                        print("cur_score is",str(cur_score))
            # update score
                if cur_score > max_score:
                    max_score = cur_score
                #print("max_score is :" + str(max_score))
                
        return max_score
        
    def maxSatisfied2(self, customers, grumpy, X):      
       ncus = 0
       nbad = 0       
       n = len(customers)
       
       for i in range(n):
           ncus += customers[i]
           if grumpy[i]:
               nbad += customers[i]
           else:
               customers[i] = 0
       
       
       best = cur = 0
       for i in range(n):
           cur += customers[i]
           if i >= X:
               cur -= customers[i-X]
           best = max(cur,best)
    
       return (ncus,nbad,best)
       
        
S = Solution()
S.maxSatisfied(c1,g1,X1) #16

S.maxSatisfied2(c1,g1,X1) #16

S.maxSatisfied(c2,g2,X2) #1
S.maxSatisfied(c3,g3,X3) #18
S.maxSatisfied(c4,g4,X4) #32
S.maxSatisfied(c5,g5,X5) #29

S.maxSatisfied(customers,grumpy,X) #29

