#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:14:01 2020

@author: nenad
"""

"""
https://leetcode.com/problems/most-common-word/
"""
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        wordsFreq = defaultdict(int)
        banned = set(banned)
        maxxFreq = 0
        maxxFreqWord = None
        chars = []
        i = 0
        n = len(paragraph)
        while i < n:
            while i < n and not paragraph[i].isalpha():
                i += 1
            while i < n and paragraph[i].isalpha():
                chars.append(paragraph[i])
                i += 1
            if len(chars) == 0:
                break
            word = "".join(chars).lower()
            chars = []
            if not word[-1].isalpha():
                word = word[:-1]
            if  word not in banned:
                freq = wordsFreq[word]
                wordsFreq[word] += 1
                if freq + 1 > maxxFreq:
                    maxxFreq = freq + 1
                    maxxFreqWord = word
            i += 1
        return maxxFreqWord
    
    def mostCommonWord(self, paragraph: str, banned) -> str:
        wordsFreq = defaultdict(int)
        banned = set(banned)
        maxxFreq = 0
        maxxFreqWord = None
        words = "".join([char.lower() if char.isalnum() else ' ' for char in paragraph ]).split()
        for word in words:
            if  word not in banned:
                freq = wordsFreq[word]
                wordsFreq[word] += 1
                if freq + 1 > maxxFreq:
                    maxxFreq = freq + 1
                    maxxFreqWord = word
           
        return maxxFreqWord
        
print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(Solution().mostCommonWord("Bob", []))
print(Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
