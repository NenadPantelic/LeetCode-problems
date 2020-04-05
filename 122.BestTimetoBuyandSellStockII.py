#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:57:20 2020

@author: nenad
"""

"""
122. Best Time to Buy and Sell Stock II

Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Problem description: 
    
    
    Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


# Time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices) -> int:
        
        # find local  minima - buy it
        # find local maxima - sell it
        i = 0
        n = len(prices)
        profit = 0
        while i < n-1:
            # find local minima
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            # we traversed over all elements
            # if values are sorted in nonincreasing order - there is no profit
            if i == n - 1:
                break
            buy = i
            i += 1
            # find local maxima
            while i < n and prices[i] >= prices[i-1]:
                i += 1
            sell = i-1
            # update profit
            profit += prices[sell] - prices[buy]
            
        return profit
    
sol = Solution()
# Test 1
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
            
# Test 2
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))