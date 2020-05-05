#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:19:44 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/first-unique-character-in-a-string/
Problem description: 
First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
# Time: O(len(s)), space: O(len(s))
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # unique chars in whole string
        uniqueChars = set()
        # map of chars and their positions - only for unique chars
        positionMap = {}
        
        for i in range(len(s)):
            char = s[i]
            if char in uniqueChars:
                if char in positionMap:
                    # remove non-duplicate
                    positionMap.pop(char)
                
            else:
                uniqueChars.add(char)
                # add char to positionMap - unique char
                positionMap[char] = i
                
        for val in positionMap:
            # return first char that was added to dictionary - dictionary preserves the order of insertion (Python 3.6+)
            return positionMap[val]
        # default case - there is no unique char
        return -1
    
sol = Solution()

# Test 1
s = "leetcode"
print(sol.firstUniqChar(s))


# Test 2
s = "aaa"
print(sol.firstUniqChar(s))


# Test 3
s = "loveleetcode"
print(sol.firstUniqChar(s))