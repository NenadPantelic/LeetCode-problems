#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:46:40 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/sqrtx/
Problem description:
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""

class Solution:
    # O(sqrt(n))
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        while True:
            val = sqrt + 1
            if val * val <= x:
                sqrt += 1
            else:
                break
        return sqrt
    # O(log(n))
    def mySqrt(self, x):
        sqrt = 0
        def binSearch(x, low, high):
            if low >= high:
                return high if high * high <= x else high - 1
            
            mid = low + (high - low) // 2
            squaredVal = mid * mid
            if squaredVal == x:
                return mid
            if squaredVal < x:
                low = mid + 1
            else:
                high = mid - 1
            return binSearch(x, low, high)
        return binSearch(x, 0, x)
                
    
    
sol = Solution()
for i in range(51):
    print(sol.mySqrt(i))
