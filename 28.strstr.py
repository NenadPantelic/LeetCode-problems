#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:46:56 2020

@author: nenad
"""

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""
# Time: rougly O(n), space: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        offset = len(needle)
        for i in range(n-offset+1):
            # take substring with offset and compare with needle
            if haystack[i:i+offset] == needle:
                return i
        # substring not found
        return -1

sol = Solution()
# Test 1
haystack = "hello"; needle = "ll"        
print(sol.strStr(haystack, needle))

# Test 2
haystack = "aaaaa"; needle = "bba"
print(sol.strStr(haystack, needle))
            