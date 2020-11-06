#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:17:53 2020

@author: nenad
"""


"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:   
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return ""
        digitMap = {"2": "abc", "3":"def", 
                    "4":"ghi","5":"jkl",
                    "6":"mno", "7":"pqrs", 
                    "8":"tuv", "9":"wxyz"}
        digitMap = {k:list(v) for k,v in digitMap.items()} # initially I wrote values as strings and I was lazy to
        # to recode that to lists xD
        memo = {}
        n = len(digits)
        def makeCombinations(digits, position):
            result = []
            if position == n - 1:
                return digitMap[digits[position]]
            currLetter = digitMap[digits[position]]
            if not position in memo:
                combinations = makeCombinations(digits, position + 1)
            else:
                combinations = memo[position]
            for letter in currLetter:        
                result.extend([letter + combination for combination in combinations])
            memo[position] = result
                
            return result
                    
        return makeCombinations(digits, 0)
    
    
# digits = "23"
# print(Solution().letterCombinations(digits))

digits = "234"
print(Solution().letterCombinations(digits))
    
    
    
    
# digits = "23"
# print(Solution().letterCombinations(digits))

digits = "234"
print(Solution().letterCombinations(digits))
    
digits = "2345"
print(Solution().letterCombinations(digits))


digits = ""
print(Solution().letterCombinations(digits))
    
                        
                    
        