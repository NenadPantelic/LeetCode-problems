#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:18:26 2021

@author: nenad
"""


"""
URL: https://leetcode.com/problems/climbing-stairs/
Description: 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
class Solution:
    def __init__(self):
        self. memo = {1:1, 2:2}
    # O(2^n)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    # apply memo
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = result
        return result

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1] * (n+1)
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        if n in self.memo:
            return self.memo[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = result
        return result
    
    
    
    
        
        
        
        
        