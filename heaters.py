# -*- coding: utf-8 -*-
"""
Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2,
and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4.
We need to use radius 1 standard, then all the houses can be warmed.
"""

houses1 = [1,2,3]
heaters1 = [2]

houses2 = [1,2,3,4]
heaters2 = [1,4]

houses3 = [1,2,3,5,15]
heaters3 = [2,30]

houses4 = [11,12,13]
heaters4 = [1,12]

houses5 = [11,12,13]
heaters5 = [1,12,15]

houses6 = [1,5]
heaters6 = [10]

houses7= [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters7 = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

houses = houses7
heaters = heaters7

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()
        N, i, maxRadius = len(heaters), 0, 0

        for house in houses:
            while i+1 < N and heaters[i+1] < house:
                i += 1
            maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))
        return maxRadius



S = Solution()
S.findRadius(houses1,heaters1)  #1
S.findRadius(houses2,heaters2)  #1
S.findRadius(houses3, heaters3) #13
S.findRadius(houses4,heaters4)  #1
S.findRadius(houses5,heaters5) #1
S.findRadius(houses6,heaters6) #9
S.findRadius(houses7,heaters7)
