# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 00:17:23 2019

@author: annameng
997. Find the Town Judge
In a town, there are N people labelled from 1 to N.  
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] 
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""
trust1 = [[1,2]]
trust2 = [[1,3],[2,3]]
trust3 = [[1,3],[2,3],[3,1]]
trust4 = [[1,2],[2,3]]
trust5 = [[1,3],[1,4],[2,3],[2,4],[4,3]]


class Solution:
    def findJudge(self, N, trust):
        if len(trust) == 0 and N ==1:
            return 1
        elif len(trust) == 1 and N == 2:
            return trust[0][1]
        else:
            num_dict = {}
            trust_from = set()
            for pair in trust:
                trust_from.add(pair[0])
                if pair[1] not in num_dict:
                    num_dict[pair[1]] = 1
                else:
                    num_dict[pair[1]] += 1
            
            # look through to find candidate
            for key in num_dict.keys():
                if num_dict[key] == N-1 and key not in trust_from:
                    return key
            return -1
                   
S = Solution()
S.findJudge(2, trust1) #2
S.findJudge(3, trust2) #3
S.findJudge(3, trust3) #-1
S.findJudge(3,trust4) #-1
S.findJudge(4,trust5) #3
S.findJudge(1,[])
                   
        
        
        
        
        
        
        
        
        
        
        
