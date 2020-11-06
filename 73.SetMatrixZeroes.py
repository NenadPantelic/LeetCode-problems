#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:36:25 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
"""
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setZeroRow(matrix, row):
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
        
        def setZeroColumn(matrix, col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
                
        m = len(matrix)
        if not m:
            return 
        n = len(matrix[0])
        i = j = 0
        modified = {"c":set(), "r":set()}
        for i in range(m):
            for j in range(n):
                if i in modified["r"] or j in modified["c"]:
                        continue
                    
                if matrix[i][j] == 0:
                    setZeroRow(matrix, i)
                    modified["r"].add(i)
            
                    setZeroColumn(matrix, j)
                    modified["c"].add(j)
                

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))
print(matrix)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(Solution().setZeroes(matrix))
print(matrix)
                    
    
        