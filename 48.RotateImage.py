#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:23:01 2020

@author: nenad
"""

"""

Problem URL: https://leetcode.com/problems/rotate-image/
Problem description: 
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return matrix
        # reverse column elements
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] =  matrix[n-i-1][j], matrix[i][j]
            
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
    
    def rotate(self, matrix) -> None:
        def isInMatrix(i, j, n):
            return 0 <= i < n and 0 <= j < n
        def swap(mat, x,y, a,b):
            mat[x][y], mat[a][b] = mat[a][b], mat[x][y]
            
        n = len(matrix)
        if n == 1:
            return matrix
        i = 0
        j = 0
        while i <= n and j < n:
            if isInMatrix(i,j, n) and isInMatrix(j,i,n):
                swap(matrix, i, j, j, i)
            j += 1
            if j >= n:
                i += 1
                j = i
                
        for row in matrix:
            row.reverse()
            

sol = Solution()     
matrix = [[1,2,3],
  [4,5,6],
  [7,8,9]
]
sol.rotate(matrix)
print(matrix)