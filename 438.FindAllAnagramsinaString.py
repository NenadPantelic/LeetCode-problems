#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:10:29 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Problem description: 

Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
# Time: O(len(s)), space: O(len(p))
# use sliding window technique - left and right pointer + overlapping 
# e.g. s = abca, p = abc
# we reached abc (abc is in the window) -> all chars used, left = 0, right = 3
# we won't observe the whole window again - we'll just kick out element at left pointer - increment left pointer
# and take the next element (update right). charsLeft will be 1, so we know we have only one char to add to have
# an anagram - bc stays in the window.
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        counter = Counter(p)
        result = []
        left, right = 0, 0
        length = len(p)
        # num of necessary characters
        charsLeft = len(p)
        while right < len(s):

            if counter[s[right]] > 0:
                charsLeft -= 1
            counter[s[right]] -= 1
            right += 1
            # we have an anagram of p
            if charsLeft == 0:
                # we used all the chars from p
                result.append(left)
            # we checked the window of length len(p)
            if right - left == length:
                if counter[s[left]] >= 0:
                    charsLeft += 1
                # move sliding window to the right and set pointers to the same position
                # reset the value of frequency of left pointer char (we no longer use it)
                counter[s[left]] += 1
                left += 1

                
        return result
            
    
sol = Solution()

# Test 1
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p))

# Test 2
s = "abab"
p = "ab"
print(sol.findAnagrams(s, p))
