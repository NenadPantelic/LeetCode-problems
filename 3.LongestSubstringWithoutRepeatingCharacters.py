#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:53:16 2020

@author: nenad
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        chars = {}
        # start index of nonduplicate stream
        start_index = 0
        # maximum obtained counter
        max_counter = 0
        for i in range(len(s)):
            # non repeating char
            if s[i] not in chars:
                chars[s[i]] = i
            else:
                # if that is not char from this window
                if chars[s[i]] < start_index:
                    # Update char position
                    chars[s[i]] = i
                    continue
                # update the max counter
                if i - start_index> max_counter:
                    max_counter = i - start_index
                # start from the position next to the position where this element appeared last time
                start_index = chars[s[i]] + 1
                # Update char position
                chars[s[i]] = i

        # update the max counter, if last element makes nonrepeating stream (+1 because last element is not included so far)
        if i - start_index + 1 > max_counter:
            max_counter = i - start_index + 1
        return max_counter
    
sol = Solution() 
# Test 1
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))

# Test 2
s = "bbbb"
print(sol.lengthOfLongestSubstring(s))   


# Test 3
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))   
             


# Test 4
s = "aab"
print(sol.lengthOfLongestSubstring(s))          

# Test 5
s = "dvdf"
print(sol.lengthOfLongestSubstring(s))  

# Test 6
s = "aabaab!bb"          
print(sol.lengthOfLongestSubstring(s))  