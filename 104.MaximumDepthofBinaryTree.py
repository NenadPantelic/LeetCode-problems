#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:41:43 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Problem description: 
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
  
sol = Solution()
   
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(sol.maxDepth(n1))

n1 = TreeNode(10)
print(sol.maxDepth(n1))

        
        
        