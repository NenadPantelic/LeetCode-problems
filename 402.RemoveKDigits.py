#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:27:38 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/remove-k-digits/
Problem description: 

Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
# Time: O(nk), space: O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # while num > 0 (we still have to remove digits) and while last added digit
            # is greater than current one (the one we're examining at the moment)
            while k > 0 and stack and stack[-1] > digit:
                # remove last added digit
                stack.pop(-1)
                # one digit less to remove
                k -= 1
            stack.append(digit)
        # while k > 0 -> our job is not done yet, we need to keep removing until k == 0
        # e.g. 111111 -> all digits will be in stack, so we'll remove k of them
        while k:
            # remove last added digit
                stack.pop(-1)
                # one digit less to remove
                k -= 1
        return "".join(stack).lstrip("0") or "0" # fancy way to return "0" if the first operand is "0" also
    
sol = Solution()

# Test 1
print(sol.removeKdigits("1432219", 3))

# Test 2
print(sol.removeKdigits("10200", 1))


# Test 3
print(sol.removeKdigits("10", 2))

# Test 4
print(sol.removeKdigits("11111", 3))