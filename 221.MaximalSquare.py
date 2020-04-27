#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:34:22 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/maximal-square/
Problem description: 
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


"""
# Time: O(m*n), space: O(m*n)
class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        if m:
           n = len(matrix[0])
        else:
            return 0
        sizeSquare = [[0 for j in range(n)] for i in range(m)]
        maxSurface = 0
        for i in range(m):
            for j in range(n):
                # sizeSquare[i][j] represents size of the square - edge length
                # where i,j position is the right bottom position -> surface of that square
                # is sizeSquare[i][j] ^ 2
                if i == 0 or j == 0:
                    sizeSquare[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "1":
                        # try to expand square above, left and diagonal
                        # pick the smallest value - reason: e.g. we can have 0 in some of
                        # elements (top, left, diagonal) so in that case this square cannot be made over that value
                        sizeSquare[i][j] = min(sizeSquare[i-1][j], sizeSquare[i][j-1],\
                                               sizeSquare[i-1][j-1]) + 1
                    else:
                        sizeSquare[i][j] = 0
                maxSurface = max(maxSurface, sizeSquare[i][j] ** 2)
        return maxSurface
    
sol = Solution()
# Test 1
matrix = ["1 0 1 0 0".split(),  "1 0 1 1 1".split(), "1 1 1 1 1".split(), "1 0 0 1 0".split()]