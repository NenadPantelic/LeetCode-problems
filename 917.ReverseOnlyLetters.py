#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:55:54 2020

@author: nenad
"""


"""
https://leetcode.com/problems/reverse-only-letters/
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        reversedChars = list(filter(lambda x:x.isalpha(), S))
        reversedChars.reverse()
        revStr = ""
        j = 0
        for i in range(len(S)):
            if not S[i].isalpha():
                revStr += S[i]
            else:
                revStr += reversedChars[j]
                j += 1
                
        return revStr
        

# Test 1
print(Solution().reverseOnlyLetters("ab-cd"))


# Test 2
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))


# Test 3
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))