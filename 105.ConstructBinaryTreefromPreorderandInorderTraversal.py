#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:43:22 2021

@author: nenad
"""


"""
URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def arrToTree(left, right):
            nonlocal preorderIndex
            if left > right: return None
            root = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            root.left = arrToTree(left, inorderMap[root.val]-1)
            root.right = arrToTree(inorderMap[root.val]+1, right)
            return root
        inorderMap = {value:i for i, value in enumerate(inorder)}
        preorderIndex = 0
        return arrToTree(0, len(inorderMap)-1)
        