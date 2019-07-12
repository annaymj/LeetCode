# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:08:42 2019

@author: annameng
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        result = [0]
        
        self.addPrimeNum(result,n)
        return result[-1]
    
    def addPrimeNum(self,result,n):
        for i in range(2,n):
            if self.isPrime(i):
                result.append(result[-1] + 1)
    
    def isPrime(self,n):
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
    
    '''Sieve of Eratosthenes
   Hint2:  As we know the number must not be divisible by any number > n / 2, 
    we can immediately cut the total iterations half by dividing only up to n / 2.
    
   Hint 3: Let's write down all of 12's factors:
       2 × 6 = 12
       3 × 4 = 12
       4 × 3 = 12
       6 × 2 = 12
      As you can see, calculations of 4 × 3 and 6 × 2 are not necessary. 
      Therefore, we only need to consider factors up to √n because, 
      if n is divisible by some number p, 
      then n = p × q and since p ≤ q, we could derive that p ≤ √n.'''
    def countPrimes2(self, n: int) -> int:
        if n < 2: return 0
        
        prime = [1]*n
        
        for i in range(2,int(n**0.5)+1):
            prime[i*i:n:i] = [0] * len(prime[i*i:n:i])
        
        return sum(prime)-2 #-2 because 0 and 1 is not a prime number
    
S = Solution()
S.countPrimes(10)
S.countPrimes2(10)