# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:41:56 2019

@author: annameng

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  
Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
"""

from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        
        for i in range(1,len(tiles)+1):
            result |= set(permutations(tiles,i))  #|= set union
            
        return len(result)
        