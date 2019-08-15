# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:05:41 2019

@author: annameng
"""

def mergeSort(l):
    if len(l) > 1:
        firstHalf = l[0:len(l)//2]
        secondHalf = l[len(l)//2:]
        
        mergeSort(firstHalf)
        mergeSort(secondHalf)
        merge(firstHalf, secondhalf, temp)
        
def merge(list1, list2, temp):
    idx1, idx2, idx3 = 0,0,0
    
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] > list2[idx2]:
            temp[idx3] = list2[idx2]
            idx2 += 1
            idx3 + = 1
        else:
            temp[idx3] = list1[idx1]
            idx1 += 1
            idx3 += 1
    
    while idx1 < len(list1):
        temp[idx3] = list1[idx1]
        idx1 += 1
    while idx2 < len(list2):
        temp[idx3] = list2[idx2]
        idx2 += 1