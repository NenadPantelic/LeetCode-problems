#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:31:15 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/number-of-islands/
Problem description:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""
# Time: O(m*n), space: O(m*n)

class Solution:
    def isSafe(self, i, j, location, visited, m, n):
        # location is in grid (in bound of grid), it's not previously visited and it represents land
        return i >= 0 and i < m and \
            j >= 0 and j < n and \
                location[i][j] == "1" and not visited[i][j]
    def DFS(self, grid, i, j, visited, m, n):
        # visit this place
        visited[i][j] = True
        # four directions - up, down, left, right
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for k in range(4):
            posY = i + moves[k][0]
            posX = j + moves[k][1]
            if self.isSafe(posY, posX, grid, visited, m, n):
                self.DFS(grid, posY, posX, visited, m, n)
    def numIslands(self, grid) -> int:
        # number of islands
        count = 0    
        m = len(grid)
        # empty matrix
        if m:
            n = len(grid[0])
        else:
            return 0
        # visited matrix
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                # examine connectivity from this position - only if this location is not checked already and 
                # this location represent land
                if not visited[i][j] and grid[i][j] == "1":
                    self.DFS(grid, i, j, visited, m, n)
                    # number of DFS calls is equal to number of islands (connected components)
                    count += 1
        return count

sol = Solution()
# Test 1
s = "11110\
11010\
11000\
00000"
grid = []
for i in range(0,len(s), 5):
    grid.append(list(s[i:i+5]))
    
#print(sol.numIslands(grid))    
    
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(sol.numIslands(grid))

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(sol.numIslands(grid))