#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:32:41 2020

@author: nenad
"""

"""
Problem description: https://leetcode.com/problems/count-and-say/
"""
class Solution:
    def countAndSay(self, n, value="1", ordinal=1):
        # value found
        if n == ordinal:
            return value
        new_val = ""
        i = 0
        length = len(value)
        # count freqs of elements grouped by their values
        while i < length:
            count = 0
            val = value[i]
            while i < length and val == value[i]:
                count += 1
                i += 1
            new_val += str(count) + val
        # go to next number
        return self.countAndSay(n, new_val, ordinal+1)
    
    
s = Solution()
for i in range(1,10):
    print(s.countAndSay(i))
        
        