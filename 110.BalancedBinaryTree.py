#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:19:33 2020

@author: nenad
"""
"""
URL: https://leetcode.com/problems/balanced-binary-tree/
Description: 
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.balanced = {}
        self.heights = {}
        
    def height(self, root):
        if root is None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return 1 + max(leftHeight, rightHeight)
    
    
 # This function should return tree if passed  tree 
 # is balanced, else false.  Time complexity should
 # be O(n) where n is number of nodes in tree */
    def isBalanced(self, root):
    
        if root is None: 
            return True
        if root in self.balanced:
            return self.balanced[root]
        if root.left in self.heights:
            leftHeight = self.heights[root.left]
        else:
            leftHeight = self.height(root.left)
            self.heights[root.left] = leftHeight

        if root.right in self.heights:
            rightHeight = self.heights[root.right]
        else:
            rightHeight = self.height(root.right)
            self.heights[root.right] = rightHeight

        self.heights[root] = 1 + max(leftHeight, rightHeight)
        self.balanced[root] = abs(leftHeight-rightHeight) <= 1  and self.isBalanced(root.left) and self.isBalanced(root.right)
        return self.balanced[root]
    

# Time: O(n), DFS based solution
    
class Solution:
    def __init__(self):
        self.result = True
        
    def isBalanced(self, root):
        if root is None:
            return True
        self._checkIfBalanced(root)
        return self.result
        
    def _checkIfBalanced(self, root):
        if root is None:
            return 0
        leftHeight = self._checkIfBalanced(root.left)
        rightHeight = self._checkIfBalanced(root.right)
        if abs(leftHeight - rightHeight) > 1:
            self.result = False
        return 1 + max(leftHeight, rightHeight)
    
    
 

n1 = TreeNode(1)
n1.right = TreeNode(2)
n1.right.right = TreeNode(3)       
print(Solution().isBalanced(n1))
class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        def height(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            return 1 + max(leftHeight, rightHeight)
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
