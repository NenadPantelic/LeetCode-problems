#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:10:36 2020

@author: nenad
"""


class Solution:
    def reverse(self, x: int) -> int:
        # preserve the sign
        sign  = 1 if x >= 0 else -1
        x = abs(x)
        new_num = 0
        l_bound = -2**31
        u_bound = 2**31-1
        # O(log_10(n))
        while x:
            new_num = new_num * 10 + x % 10
            # integer overflow - in Python it is safe to check this even at the end
            if new_num < l_bound or new_num > u_bound:
                return 0
            x //= 10
        
        return sign * new_num
    
s = Solution()
# Test 1
num = 123
print(s.reverse(num))


# Test 2
num = 120
print(s.reverse(num))


# Test 3
num = -321
print(s.reverse(num))

    
# Test 4
num = -2**40
print(s.reverse(num))

# Test 5
num = 1534236469
print(s.reverse(num))
    
