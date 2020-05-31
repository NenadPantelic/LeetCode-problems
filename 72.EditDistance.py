#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:16:07 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/edit-distance/
Problem description: 
Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
# Time and space: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for o in range(m+1)] for j in range(n+1)]
        # default case, when one the strings is empty
        # so table, looks like
        # 0   1   2   3   4......m-1
        # 1
        # 2
        # 3
        # ...
        # n-1
        for i in range(n+1):
            dp[i][0] = i
        
        for i in range(m+1):
            dp[0][i] = i
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # if word[j-1] == word[i-1], current chars are equal, just use the previous state (left diagonal)
                # because that's the value (case) when we omit current chars from both strings 
                # e.g. horse, rose -> we compare s from word1 and s from word2 - they're the same, so we use the value
                # from minDistance(hor, ro)
                # else: use the best value  min(left, top, left diagonal) -> positions reflect removal, insertion, replacement 
                # and add 1 (we need to replace the current char to get target one)
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        # result is at bottom right corner of dp table
        return dp[-1][-1]
    
    
sol = Solution()

# Test 1
word1 = "horse"; word2 = "ros"
print(sol.minDistance(word1, word2))


# Test 2
word1 = "intention"; word2 = "execution"
print(sol.minDistance(word1, word2))

# Test 3
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
print(sol.minDistance(word1, word2))

# Test 3
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"
print(sol.minDistance(word1, word2))