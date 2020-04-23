#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:04:15 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/bitwise-and-of-numbers-range/
Problem description: 
Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

"""
from math import log, floor
class Solution:
    # TLE
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m ==0 or n == 0:
            return 0
        res = m
        for i in range(m+1, n+1):
            res &= i
        return res
  
# General idea:
# 1. find MSB positions of both numbers:
#   a) if MSB positions are different return current result (initially it is equal to zero)
#   b) if they're equal, add 2**MSB_position to result and subtract that value from both numbers
#   c) check if m = 0 or n = 0 after subtraction -> return result 
# 2. repeat these steps until case a) or c) is fullfiled
    
class Solution:
    # Time: O(log(n)), space: O(1) -> worst case all one's in bin representation of both number and numbers are same
    # e.g. 31 - 11111 and 11111
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # on of values is zero - zero nullifies every value in AND operation
        if m == 0 or n == 0:
            return 0
        # result
        res = 0
        while True:
            # get MSB position
            posMsbM = log(m, 2)
            posMsbN = log(n, 2)
            # if MSB positions are different return result - at first that is 0
            if floor(posMsbM) != floor(posMsbN):
                return int(res)
            # get MSB weight 
            weight =  2 ** floor(posMsbM)
            # add weight to final result
            res += weight
            # subtract weight from both values
            m -= weight
            n -= weight
            # if some value goes negative or zero - return result (for log's safe domain)
            if m <= 0 or n <= 0:
                return int(res)
            
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # remove last bit - shift to right until we get m = n
        shiftCount = 0
        while m != n:
            m >>= 1
            n >>= 1
            shiftCount += 1
        return m << shiftCount
sol = Solution()
# Test 1
print(sol.rangeBitwiseAnd(5,7))

# Test 2
print(sol.rangeBitwiseAnd(0,1))