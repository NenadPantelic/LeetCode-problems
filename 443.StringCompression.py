#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:53:21 2020

@author: nenad
"""


"""
https://leetcode.com/problems/string-compression/
"""

class Solution:
    def compress(self, chars) -> int:
        i = 0
        n = len(chars)
        while i < n:
            #start = chars[i]
            startIndex = i
            i += 1
            while i < n and chars[startIndex] == chars[i]:
                i += 1
            else:
                length = i - startIndex 
                if length != 1:
                    lengthStr = str(length)
                    for j in range(len(lengthStr)):
                        chars[startIndex + 1 + j] = lengthStr[j]
                    for j in range(startIndex + 1 + len(lengthStr), i):
                        chars[j] = None
        for i in range(n-1, -1, -1):
            if chars[i] is None:
                chars.pop(i)
                        
        return len("".join(chars))
    
    def compress(self, chars) -> int:
        i = 0
        n = len(chars)
        write = 0
        while i < n:
            #start = chars[i]
            startIndex = i
            i += 1
            while i < n and chars[startIndex] == chars[i]:
                i += 1
            else:
                length = i - startIndex 
                chars[write] = chars[startIndex]
                if length != 1:
                    #chars[write] = chars[startIndex]
                    write += 1
                    lengthStr = str(length)
                    for j in range(len(lengthStr)):
                        chars[write] = lengthStr[j]
                        write += 1
                else:
                    write += 1
        return write
    
# Test 1
chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))    

# Test 2
chars = ["a"]
print(Solution().compress(chars))    

# Test 3
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))        

# Test 4
chars = ["a","a","a","b","b","a","a"]
print(Solution().compress(chars))    

# Test 5
chars = ["a","a","a","a","a","b"]
print(Solution().compress(chars))   

