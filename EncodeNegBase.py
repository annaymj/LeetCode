# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:29:59 2019

@author: annayu
"""

def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s
    
    
def EncodeNegBase(n, b): #Converts from decimal
    if n == 0:
        return "0"
    out = []
    while n != 0:
        n, rem = divmod(n, b)
        if rem < 0:
            n += 1
            rem -= b
        out.append(rem)
    return "".join(map(str, out[::-1]))
    

def DecodeNegBase(nstr, b): #Converts to decimal
	if nstr == "0":
		return 0
 
	total = 0
	for i, ch in enumerate(nstr[::-1]):
		total += int(ch) * b**i
	return total
 
A = [0,1,1,1,1,1] 

def prefixesDivBy5(A):
    n = len(A)
    ans = [False] * n
    val = 0
    
    for i, num in enumerate(A):
        val = (val * 2 + num) % 5
        if val == 0:
            ans[i] = True
    return ans