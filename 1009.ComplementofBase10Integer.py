#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:17:21 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
Problem description: 
Number Complement
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # k bits = bit number necessary for num representation
        # Find first complement = biggest number that can be made with k bits - num
        bitNum = len(bin(N)[2:])
        return 2 ** bitNum - 1 - N
    
sol = Solution()
# Test 1
print(sol.bitwiseComplement(5))

# Test 2
print(sol.bitwiseComplement(1))

# Test 3
print(sol.bitwiseComplement(0))
# Test 4
print(sol.bitwiseComplement(31))