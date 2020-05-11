#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:26:40 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/flood-fill/
Problem description: 
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

"""
# Time: O(m * n), space: O(m * n)
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m, n = len(image), len(image[0])
        visited = [[False] * n for _ in range(m)]
        def isSafe(row, col, m, n, val, image,  visited):
            # check if:
            #  1) the position (row, col)  is valid - inside image
            #  2) the position (row, col)  is unvisited
            #  3) the colors match - image[row][col] == val
            return row >= 0 and row < m and col >= 0 and col < n and \
                visited[row][col] == False and val == image[row][col]
            
        def simulate(image, sr, sc, newColor, visited):
            val = image[sr][sc]
            # this position is visited now
            visited[sr][sc] = True
            # check top neighbour
            if isSafe(sr-1, sc, m, n, val, image, visited): 
                simulate(image, sr-1, sc, newColor, visited)
        
            # check bottom neighbour
            if isSafe(sr+1, sc, m, n, val, image, visited): 
                simulate(image, sr+1, sc, newColor, visited)
                
            # check left neighbour
            if isSafe(sr, sc-1, m, n, val, image, visited): 
                simulate(image, sr, sc-1, newColor, visited)
                
            # check right neighbour
            if isSafe(sr, sc + 1, m, n, val, image, visited): 
                simulate(image, sr, sc + 1, newColor, visited)
            # set new value of color for current position
            image[sr][sc] = newColor
            return 
    
        simulate(image, sr, sc, newColor, visited)
        return image
        
sol = Solution()

# Test 1
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1; sc = 1; newColor = 2
sol.floodFill(image, sr, sc, newColor)
print(image)