#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:17:10 2020

@author: nenad
"""

# Time: O(n * min(len(all words)))
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        i = 0
        minLen = len(min(strs, key=len))
        firstWord = strs[0]
        commonPrefix = ""
        while i < minLen and all(val[i] == firstWord[i] for val in strs):
            commonPrefix += firstWord[i]
            i += 1
        return commonPrefix
    
    
# Test 1
print(Solution().longestCommonPrefix(["flower","flow","flight"]))


# Test 1
print(Solution().longestCommonPrefix(["dog","racecar","car"]))