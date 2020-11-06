#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:03:14 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/interleaving-string/
Problem description: Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

"""
# Time: O(m*n)
class Solution:
    def __init__(self):
        self.cache = set()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.cache = set()
        def checkInterleave(s1: str, s2: str, s3: str):
            if s1 is None or s2 is None or s3 is None:
                return False
            if (s1, s2) in self.cache:
                return False
            
            if len(s1) + len(s2) != len(s3):
                return False
            if not s1 or not s2 or not s3:
                return s1 + s2 == s3
            # if len(s1) == 0:
            #     return s2 == s3
            # if len(s2) == 0:
            #     return s1 == s3
            if (s1, s2) in self.cache:
                return False
            if s1[0] != s3[0] and s2[0] != s3[0]:
                return False
            if s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
                return True
            if s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]):
                return True
            self.cache.add((s1, s2))
            return False
        return checkInterleave(s1, s2, s3)
        
            

sol = Solution()

# Test 1
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
print(sol.isInterleave(s1, s2, s3))

# Test 2
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
print(sol.isInterleave(s1, s2, s3))

# Test 3
s1 = ""; s2 = ""; s3 = " "
print(sol.isInterleave(s1, s2, s3))

# Test 4
s1 = "aa"; s2 = "ab"; s3 = "aaba"
print(sol.isInterleave(s1, s2, s3))

# Test 5
s1 = "aabc"
s2 = "abad"
s3 = "aabadabc"
print(sol.isInterleave(s1, s2, s3))