#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:38:23 2020

@author: nenad
"""


class Solution:
    def checkMapping(self, s, t):
    # assume s and t have the same length
        char_map = {}
        for i in range(len(s)):
            val = char_map.get(s[i])
            if val:
                if val != t[i]:
                    return False
            else:
                char_map[s[i]] = t[i]
                
        return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.checkMapping(s,t) and self.checkMapping(t, s) 
        
s =Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("egg", "abc"))
print(s.isIsomorphic("paper", "title"))