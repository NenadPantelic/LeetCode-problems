#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:33:17 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/diameter-of-binary-tree/
Problem descirption: 
    Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time - O(n), space O(n)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diam = 0
        self.diameterOfNode(root)
        return self.diam
    def diameterOfNode(self, node, diam = 0):
        if node is None:
            return 0
        ldiam = self.diameterOfNode(node.left, self.diam)
        rdiam = self.diameterOfNode(node.right, self.diam)
        self.diam = max(self.diam, ldiam + rdiam)
        return max(ldiam, rdiam)+1
# Version 2
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diam = 1
        self.diameterOfNode(root)
        return self.diam-1
    def diameterOfNode(self, node):
        if node is None:
            return 0
        ldiam = self.diameterOfNode(node.left)
        rdiam = self.diameterOfNode(node.right)
        self.diam = max(self.diam, ldiam + rdiam+1)
        return max(ldiam, rdiam)+1