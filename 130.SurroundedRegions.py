#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:29:34 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/surrounded-regions/
Problem description: 
Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
class Solution:
    def __init__(self):
        self.border = False
    def isSafe(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
    
    def flip(self, board, visited, x, y, m, n):
        if self.isSafe(x, y, m, n):
          if board[x][y] == "X":
              return
          board[x][y] = "X"
          self.flip(board, visited, x+1, y, m, n)
          self.flip(board, visited, x-1, y, m, n)
          self.flip(board, visited, x, y+1, m, n)
          self.flip(board, visited, x, y-1, m, n)
    def dfs(self, board, visited, x, y, m, n):
        if self.isSafe(x, y, m, n) and not visited[x][y] and board[x][y] == "O":
            if x in (0, m-1) or y in (0, n-1):
                self.border = True
            visited[x][y] = True
            self.dfs(board, visited, x+1, y, m, n)
            self.dfs(board, visited, x-1, y, m, n)
            self.dfs(board, visited, x, y+1, m, n)
            self.dfs(board, visited, x, y-1, m, n)
            
        
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if visited[i][j] or board[i][j] == "X": 
                    continue
                self.border = False
                self.dfs(board, visited, i, j, m, n)
                if not self.border:
                    self.flip(board, visited, i, j, m, n)
                self.border = True
        
        self.border = False
        
sol = Solution()

# Test 1
s = "X X X X \
X O O X \
X X O X \
X O X X" .split()

s = [s[i:i+4] for i in range(0,16, 4)]
sol.solve(s)
print(s)