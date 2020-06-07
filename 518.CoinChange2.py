#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:58:30 2020

@author: nenad
"""


"""
Problem URL:https://leetcode.com/problems/coin-change-2/
Problem description: 
Coin Change 2
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

"""
# Time and space: O(amount * len(coins))
class Solution:
    def change(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount+1)] for i in range(n+1)]
        # amount = 0  can be with every coin
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                # coin can be used to make current amount (amount is greater than or equal to coin value)
                if coins[i-1] <= j:
                    # case - exclude ith coin  plus case - include ith coin (use value = current amount - ith coin -> we should make this amount now)
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    # use the previous state (without this coin in game)
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
    
sol = Solution()

# Test 1
amount = 5; coins = [1, 2, 5]
print(sol.change(amount, coins))

# Test 2
amount = 3; coins = [2]
print(sol.change(amount, coins))

# Test 3
amount = 10; coins = [10] 
print(sol.change(amount, coins))