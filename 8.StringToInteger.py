#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:49:15 2020

@author: nenad
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        num = 0
        sign = 1
        first_char = False
        for char in str:
            # char is digit
            if char.isdigit():
                num = num * 10 + int(char)
                first_char = True
            # first non-whitespace char
            elif not first_char:
                # valid options are whitespace, and +-
                if char == " ": 
                    continue
                elif char == "+":
                    sign = 1
                    first_char = True
                elif char == "-":
                    sign = -1
                    first_char = True
                else:
                    break                
            else:
                break  
                
        num = sign * num
        # value not in integer range
        if num < -2**31:
            return -2**31
        if num > 2 ** 31 - 1:
            return 2 ** 31-1
        return num
    
sol = Solution()
# Test 1
print(sol.myAtoi("42"))


# Test 2
print(sol.myAtoi("-42"))


# Test 3
print(sol.myAtoi("4193 with words"))


# Test 4
print(sol.myAtoi("words and 987"))

# Test 5
print(sol.myAtoi("-91283472332"))

# Test 6
print(sol.myAtoi("3.145926"))                    

# Test 7
print(sol.myAtoi("   +0 123"))   

# Test 8
print(sol.myAtoi("-   234"))  

# Test 9
print(sol.myAtoi("0-1"))  

# Test 10
print(sol.myAtoi("++3")) 

# Test 11
print(sol.myAtoi(".1"))

# Test 12
print(sol.myAtoi("+1"))

