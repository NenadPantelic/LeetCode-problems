#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:24:10 2020

@author: nenad
"""
"""
Problem URL: https://leetcode.com/problems/longest-common-subsequence/
Problem description:
 Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

"""
# Time and space: O(len1*len2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0 for j in range(len2+1)] for i in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1, len2+1):
                # we start at second row and second col of dp table
                # first row and first col are trivial cases -> one of strings is empty
                # so element at position (i,j) in dp table is result of comparing
                # subsequences text1[:i] and text2[:j] -> when we compare text1[i] and text2[j], that 
                # will be written in dp[i+1][j+1]
                # text1[i] == text2[j] - case -> dp[i-1][j-1] is LCS value of text1[:i] and text2[:j] - so without current chars, +1 because current chars are equal
                # e.g. abcf and bf -> we compare f and f -> they're the same
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # else get max value between LCS(text1[:i], text2[:j+1]) and LCS(text1[:i+1], text2[:j]) - 
                # e.g. abc and bf -> we compare c and f -> they're not equal, so use greater of
                # LCS(ab, bf) and LCS(abc, b).
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # get top right value from dp table                    
        return dp[-1][-1]
    

sol = Solution()
# Test 1
text1 = "abcde"; text2 = "ace" 
print(sol.longestCommonSubsequence(text1, text2))

# Test 2
text1 = "abc"; text2 = "abc"
print(sol.longestCommonSubsequence(text1, text2))

# Test 3
text1 = "abc"; text2 = "def"
print(sol.longestCommonSubsequence(text1, text2))     