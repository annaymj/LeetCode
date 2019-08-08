# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:22:10 2019

@author: annameng
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to 
dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) 
- that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, 
and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

"""

dominoes = [[1,2],[2,1],[3,4],[5,6]]   #1
dominoes2 = [[1,2],[2,1],[3,4], [3,4],[5,6]] #2
dominoes3 = [[1,2],[2,1],[2,1],[3,4],[5,6]] #3


class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        comb = {}
        result = 0
        
        for i in range(len(dominoes)):
            pair = sorted(dominoes[i])
            tuple_pair = tuple(pair)
            
            if tuple_pair  in comb.keys():
                comb[tuple_pair] += 1
            else:
                comb[tuple_pair] = 1
        
        for key in comb.keys():
            val = comb[key]
            if val > 1:
                result += val * (val - 1)/2
        
        return int(result)

S = Solution()
S.numEquivDominoPairs(dominoes)
S.numEquivDominoPairs(dominoes2)
S.numEquivDominoPairs(dominoes3)