#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:04:16 2020

@author: nenad
"""


"""
Problem URL:  https://leetcode.com/problems/fibonacci-number/
Problem description:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.   
"""

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
    
    def fib(self, N):
        memo = {0:0, 1:1}
        def fibUtil(N, memo):
            if N in memo:
                return memo[N]
            else:
                result = fibUtil(N-1, memo) + fibUtil(N-2, memo)
                memo[N] = result
                return result
        return fibUtil(N, memo)
            
sol = Solution()
for i in  range(10):
    print(sol.fib(i))