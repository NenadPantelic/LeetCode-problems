#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:45:58 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/ransom-note/
Problem description:
Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""
# Time: O(len(ransomNote) + len(magazine)), space: O(len(magazine))
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterMagazineLetters = Counter()
        
        for letter in magazine:
            counterMagazineLetters[letter] += 1
        
        for letter in ransomNote:
            val = counterMagazineLetters.get(letter, 0)
            if val <= 0:
                return False
            counterMagazineLetters[letter] -= 1
        
        return True
    def canConstruct(self, ransomNote, magazine):
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for letter in ransomNoteCounter:
            if ransomNoteCounter[letter] > magazineCounter.get(letter, 0):
                return False
        return True
    
    
sol = Solution()

# Test 1
print(sol.canConstruct("a", "b"))
            
# Test 2
print(sol.canConstruct("aa", "ab"))


# Test 3
print(sol.canConstruct("aa", "aab"))