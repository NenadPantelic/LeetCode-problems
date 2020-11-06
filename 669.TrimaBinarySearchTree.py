#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:49:02 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/trim-a-binary-search-tree/
Problem description: 
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        if L > root.val:
            return self.trimBST(root.right, L, R)
        if R < root.val:
            return self.trimBST(root.left, L, R)

sol = Solution()
        
n1 = TreeNode(3)
n2 = TreeNode(0)
n3 = TreeNode(4)
n4 = TreeNode(2)
n5 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.right = n4
n4.left = n5
head = print(sol.trimBST(n1, 1, 3))
        