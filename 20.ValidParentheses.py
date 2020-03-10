#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:31:10 2020

@author: nenad
"""

"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

# Time and space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(":")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            # push the opening bracket to stack
            if char in "([{":
                stack.append(char)
            else:
                # there is no complementary open bracket for this close bracket
                if len(stack) == 0:
                    return False
                val = mapping[stack.pop(-1)]
                # mapping doesn't fit e.g. ( and ]
                if char != val:
                    return False
        # there are more open brackets than closing
        if len(stack) > 0:
            return False
        # otherwise
        return True

sol = Solution()   
    
# Test 1
print(sol.isValid("()"))        

# Test 2
print(sol.isValid("()[]{}"))        

# Test 3
print(sol.isValid("((())"))        

# Test 1
print(sol.isValid("(}[](()}"))            
                               
                