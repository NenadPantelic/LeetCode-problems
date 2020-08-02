#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:07:24 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/generate-parentheses/
Problem description: 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
# Time and space: O(2^n)
class Solution:
    def generateParenthesis(self, n: int):
        def generateParenthesisCombination(n, leftParenthesisCount = 0, rightParenthesisCount = 0, combination = "", allCombinations=[]):
            if leftParenthesisCount < n:
                generateParenthesisCombination(n, leftParenthesisCount + 1, rightParenthesisCount, combination + "(", allCombinations)
            # to assure that every combination is valid -> close the opened bracket   
            if rightParenthesisCount < leftParenthesisCount:
                generateParenthesisCombination(n, leftParenthesisCount, rightParenthesisCount + 1, combination + ")", allCombinations)
            if leftParenthesisCount == rightParenthesisCount == n:
                allCombinations.append(combination)
        combinations = []
        generateParenthesisCombination(n, allCombinations = combinations)
        return combinations
            
sol = Solution()
print(sol.generateParenthesis(3))