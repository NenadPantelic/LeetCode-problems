#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:22:30 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/counting-bits/
Problem description: 

Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
   Hide Hint #1  
You should make use of what you have produced already.
   Hide Hint #2  
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
   Hide Hint #3  
Or does the odd/even status of the number help you in calculating the number of 1s?
"""
# Time: O(n), space: O(n)
class Solution:
    def countBits(self, num: int):
        # default casee
        if num == 0:
            return [0]
        # result list
        result = [0]
        offset = 1
        val = 1
        # pattern of bits is repeating
        # 1 bit = 0, 1
        # 2 bits = 10, 11
        # 3 bits = 100, 101, 110, 111
        # 4 bits = 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
        # so when we complete all numbers that can be made with k bits, for nums that can be made with k+1 bits
        # we use all of the previous values and we add the leading 1. So, 
        # number e.g we can get number of ones in number 9 when we check how many 1s we need to make 9-8 = 1 and 
        # one more 1 -> 9-8 = 1 -> bin(1) = 1, so we add one more 1 to make 9 -> bin(10001)
        # In general - num of 1s in some num = num of 1s in (num - (greatest number that is power of two that is less than num)) + 1
        while val <= num:
            # we add +1 for the most significant bit
            result.append(result[val-offset]+1)
            val += 1
            if val == 2 * offset:
                # update offset - double it -> 1, 2, 4, 8, 16, 32, 64, 128...
                offset <<= 1
            
        return result
    
sol = Solution()

# Test 1
print(sol.countBits(2))


# Test 2
print(sol.countBits(5))

# Test 3
print(sol.countBits(13))
        
# Test 4
print(sol.countBits(1))


# Test 5
print(sol.countBits(0))