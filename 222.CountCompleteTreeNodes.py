#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:14:25 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/count-complete-tree-nodes/
Problem description: 
Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        
    def countNodes(self, root: TreeNode) -> int:
        def preorderCount(root):
            if not root:
                return 
            self.count += 1
            preorderCount(root.left)
            preorderCount(root.right)
        
        preorderCount(root)   
        return self.count
    