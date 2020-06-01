#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:22:05 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/invert-binary-tree/
Problem description:
Invert Binary Tree
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return
        # store left and right descendants
        left  = root.left
        right = root.right
        # invert the tree
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root

        
sol = Solution()

def preorder(node):
    if not node:
        return 
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

# Test 1
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

node = sol.invertTree(n1)
preorder(node)