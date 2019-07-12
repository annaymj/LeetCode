# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:54:06 2019

@author: annameng
Given a list of scores of different students, return the average score of each 
student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  
The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
"""
import math
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

class Solution:
    def highFive(self, items):
        score = {}
        result= []
        
        for i in items:
            if i[0] not in score:
                score[i[0]] = [i[1]]
            else:
                score[i[0]].append(i[1])
           
        
        for key in score.keys():
            score_list = sorted(score[key],reverse = True)
            avg = math.floor(sum(score_list[:5])/5)
            result.append([key,avg])
        
        return result

S = Solution()
S.highFive(items)