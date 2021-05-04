#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:22:52 2021

@author: nenad
"""
"""
URL: https://leetcode.com/problems/longest-palindromic-substring/
Description: 
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
based on: https://leetcode.com/problems/longest-palindromic-substring/discuss/3060/(AC)-relatively-short-and-very-clear-Java-solution
"""

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLenSubstr = ""
        def isPalindrome(s, i, j):
            if i < 0: return False
            if j in (i, i+1): return s[i] == s[j]
            return s[i] == s[j] and isPalindrome(s, i+1, j-1)
        currLen = 0
        for i in range(n):
            if (isPalindrome(s, i-currLen-1, i)):
                maxLenSubstr = s[i-currLen-1:i+1]
                currLen += 2
            elif (isPalindrome(s, i-currLen, i)):
                maxLenSubstr = s[i-currLen:i+1]
                currLen += 1
        return maxLenSubstr