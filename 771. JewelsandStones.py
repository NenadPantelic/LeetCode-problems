#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:40:07 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/jewels-and-stones/
Problem desription: 
Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

"""
# Time: O(max(len(S), len(J))), space: O(max(len(S), len(J)))

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        charsInJ = set(list(J))
        counter = 0
        for char in S:
            if char in charsInJ:
                counter += 1
        return counter
    
    
sol = Solution()
# Test 1
J = "aA"; S = "aAAbbbb"
print(sol.numJewelsInStones(J, S))

# Test 1
J = "z"; S = "ZZ"
print(sol.numJewelsInStones(J, S))
