# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:32:22 2018
ou're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

:type J: str
:type S: str
:rtypr: int

@author: annameng
"""
class Solution(object):
    def numJewelsInStones(self,J,S):
        count = 0
        for char in J:
            count += S.count(char)
        return count
    
    def numJewelsInStones2(self,J,S):
       # setJ = set(J)
        return sum(s in J for s in S)
    
    def numJewelsInStones3(self,J,S):
       # setJ = set(J)
        return sum(map(S.count,J))
       
def main():
    testSolution = Solution() 
    
    # Test method numJewelsInStones
    J = "aA"; S="aAAbbb"
    result = testSolution.numJewelsInStones3(J,S)
    print('\nTest case 1: \nThe number of Jewels in Stones is')
    print(result)
    
    J = "z"; S="ZZ"
    result = testSolution.numJewelsInStones3(J,S)
    print('\nTest case 2: \nThe number of Jewels in Stones is')
    print(result)

main()