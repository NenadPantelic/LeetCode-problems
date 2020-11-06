#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:52:02 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/longest-palindromic-subsequence/
Problem description: 
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for l in range(1, n+1):
            for i in range(n-l+1):
                if i == (i + l-1):
                    # default case - length of subsequence is 0
                    dp[i][i+l-1] = 1
                else:
                    # first and last character of subsequence are the same
                    if s[i] == s[i+l-1]:
                        dp[i][i+l-1] = dp[i+1][i+l-2] + 2
                    # take longer pal. subsequence of these two options - s[i:j-1], s[i+1:j]
                    else:
                        dp[i][i+l-1] = max(dp[i][i+l-2], dp[i+1][i+l-1])
        return dp[0][-1]

sol = Solution()

# Test 1
s = "agbdba"
print(sol.longestPalindromeSubseq(s))

# Test 2
s = "bbbab"
print(sol.longestPalindromeSubseq(s))

# Test 3    
s = "cbbd"
print(sol.longestPalindromeSubseq(s))
                
                
        