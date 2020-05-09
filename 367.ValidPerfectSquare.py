#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:22:33 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/valid-perfect-square/
Problem description: 
 Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


"""
# Time: O(sqrt(n)), space: O(1)
class Solution:    
    def isPerfectSquare(self, num: int) -> bool:
        if num < 10:
            return num in (1, 4, 9)
        lastDigit = num % 10
        # simplest explanation - values of digits squared
        # number must have some of this values as it's last digit
        # 1 * 1 = 1
        # 2 * 2 = 4
        # 3 * 3 = 9
        # 4 * 4 = 16
        # 5 * 5 = 25
        # 6 * 6 = 36
        # 7 * 7 = 49
        # 8 * 8 = 64
        # 9 * 9 = 81
        # 0 * 0 = 0
        # all possible outcomes - {0, 1, 4, 5, 6, 9}
        if lastDigit not in (1, 4, 5, 6, 9, 0):
            return False
        val = 4
        while val * val < num:
            val += 1
        return val * val == num
        
    
    

    
    
sol = Solution()

# Test 1
print(sol.isPerfectSquare(16))


# Test 2
print(sol.isPerfectSquare(14))