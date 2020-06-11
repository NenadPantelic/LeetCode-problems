#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:00:19 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/is-subsequence/
Problem description: 
Is Subsequence
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""
# Time: O(min(len(s), len(t))), space: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        i, j = 0, 0
        while i < lenS and j < lenT:
            # chars are the same, observe next char of s
            if s[i] == t[j]:
                i += 1
            j += 1
        # if i == lenS that means we found every char of s in t
        return i == lenS

sol = Solution()
 
# Test 1
s = "abc"; t = "ahbgdc"
print(sol.isSubsequence(s, t))                

# Test 2
s = "axc"; t = "ahbgdc"
print(sol.isSubsequence(s, t))  