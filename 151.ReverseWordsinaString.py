#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:39:01 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/reverse-words-in-a-string/
Problem description:
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
# Time and space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        reversedChars = list(reversed(s))
        start = stop = 0
        words = []
        word = []
        for i in range(len(reversedChars)):
            if reversedChars[i] == " ":
                stop = i
                if stop != start:
                    words.append("".join(word))
                    word = []
                start = i + 1
            else:
                word.insert(0, reversedChars[i])
            
        words.append("".join(word))
        return " ".join(words)
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
    
sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s))
    
s = "  hello world!  "
print(sol.reverseWords(s))

s = "a good   example"
print(sol.reverseWords(s))