#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:12:07 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkIsPal(s, l, r):
            
            if r <= l:
                return True
            if not s[l].isalnum():
                return checkIsPal(s, l+1, r)
            if not s[r].isalnum():
                return checkIsPal(s, l, r-1)
            return s[l] == s[r] and checkIsPal(s, l+1, r - 1)
        return checkIsPal(s.lower(), 0, len(s)-1)
    
    def isPalindrome(self, s):
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
                
            while j >= 0 and not s[j].isalnum():
                j -= 1
            
            if i >= j:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    
        
s = "1b1"
print(Solution().isPalindrome(s))

s = "0P"
print(Solution().isPalindrome(s))