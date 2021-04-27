#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:22:42 2021

@author: nenad
"""
"""
URL: https://leetcode.com/problems/merge-two-binary-trees/
Description:
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
 

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
class Solution:
    root = None
    def _createNode(self, node1, node2):
        if node1 is None and node2 is None:
            return None
        leftVal = node1.val if node1 else 0
        rightVal = node2.val if node2 else 0
        return TreeNode(leftVal+rightVal)

    def _getChild(self, node, child="left"):
        if node is None: return None
        return node.left if child == "left"else node.right
        
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        Solution.root = None
        def _mergeTrees(root1, root2):
            root = self._createNode(root1, root2)
            if Solution.root is None:
                Solution.root = root
            if root:
                root.left = _mergeTrees(self._getChild(root1), self._getChild(root2))
                root.right = _mergeTrees(self._getChild(root1, "right"), self._getChild(root2, "right"))
            return root
        _mergeTrees(root1, root2)
        return Solution.root
    
   
        
        
        