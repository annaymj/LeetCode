# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:10:32 2019

@author: annayu
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

class Solution:
    def maxProfit1(self, prices: 'List[int]') -> 'int':
        max_profit = 0
            
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]  - prices[i] > max_profit:
                    max_profit = prices[j]  - prices[i]
        return max_profit
        
    # faster solution 
    def maxProfit2(self,prices:'list[int]') -> 'int':

       # check if prcies is none
       if not prices:
           return 0
        
        max_profit = 0
        
        buy_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - buy_price)
            buy_price = min(buy_price, price)
        return max_profit
    
    # the fastest solution    
    def maxProfit3(self,prices:'list[int]') -> 'int':
        
        max_profit = 0
        low_price = sys.maxsize
        
        for price in prices:
            if price - low_price > max_profit:
                max_profit = price - low_price
            if price < low_price:
                low_price = price
        return max_profit
        
            
    
S = Solution()
S.maxProfit3(prices1)

S.maxProfit3(prices2)