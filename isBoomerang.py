# -*- coding: utf-8 -*-
"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.
"""

points = [[0,0],[0,2],[2,1]]  # True
points2 = [[0,0],[1,0],[2,2]] # True
points3 = [[0,0],[2,1],[2,1]] # False
points4 = [[0,1],[1,1],[2,1]] #False


def isBoomerang(points) -> bool:
    
    ax, ay = points[0]
    bx, by = points[1]
    cx, cy = points[2]
    
    l1 = bx - ax, by- ay
    l2 = cx - ax, cy- ay
    return l2[1]* l1[0] != l2[0] * l1[1]
  