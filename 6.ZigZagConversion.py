#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:06:43 2020

@author: nenad
"""

# Time: O(n), space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # trivial case
        if numRows == 1:
            return s
        zigZagList = [[] for i in range(min(len(s),numRows))]
        pos = 0
        offset = 1
        for i in range(len(s)):
            zigZagList[pos].append(s[i])
            pos += offset
            # change direction (to zag :-)))
            if pos == numRows-1:
                offset = -1
                #pos -= 1
            # change direction (to zig :-)))
            if pos == 0:
                offset = 1
 
        rowWiseStr = ""
        for zz in zigZagList:
            rowWiseStr += "".join(zz)
        return rowWiseStr
    
sol = Solution()    
# Test 1
s = "paypalishiring"
numRows = 4        
print(sol.convert(s,numRows))


# Test 2
s = "paypalishiring"
numRows = 3
print(sol.convert(s,numRows))


# Test 3
s = "AB"
numRows = 1
print(sol.convert(s,numRows))