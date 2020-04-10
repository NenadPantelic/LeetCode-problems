#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:32:28 2020

@author: nenad
"""


"""

Problem description: https://leetcode.com/problems/backspace-string-compare/
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    # Time: O(n), space:O(n)
    def filterString(self, S):
        stack = []
        # put to stack every char that's not equal to "#", remove from stack when char is equal to "#"
        for i in range(len(S)):
            if S[i] != "#":
                stack.append(S[i])
            else:
                if len(stack):
                    stack.pop(-1)
        newS = "".join(stack)
        # return filtered string
        return newS
    def backspaceCompare(self, S: str, T: str) -> bool:
        # compare filtered strings
        return self.filterString(S) == self.filterString(T)
    
sol = Solution()

# Test 1
S = "ab#c"; T = "ad#c"
print(sol.backspaceCompare(S,T))
# Test 2
S = "ab##"; T = "c#d#"
print(sol.backspaceCompare(S,T))
# Test 3
S = "a##c"; T = "#a#c"
print(sol.backspaceCompare(S,T))
# Test 4
S = "a#c"; T = "b"
print(sol.backspaceCompare(S,T))

# Test 5
S = "bxo#j##tw"; T = "bxj##tw"
print(sol.backspaceCompare(S,T))
