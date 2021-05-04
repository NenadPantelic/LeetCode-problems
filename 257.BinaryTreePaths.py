#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:17:56 2021

@author: nenad
"""
"""
URL: https://leetcode.com/problems/binary-tree-paths/
Description:
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def findPaths(root, path):
            nonlocal paths
            if root is None:
                return None
            if root.left is None and root.right is None:
                paths.append(f'{path}->{root.val}'[2:])
            findPaths(root.left, f'{path}->{root.val}')
            findPaths(root.right, f'{path}->{root.val}')
        findPaths(root, "")
        return paths
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def findPaths(root, path):
            nonlocal paths
            if root is None:
                return None
            if root.left is None and root.right is None:
                paths.append(f'{path}->{root.val}'[2:])
            findPaths(root.left, f'{path}->{root.val}')
            findPaths(root.right, f'{path}->{root.val}')
        findPaths(root, "")
        return paths
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def findPaths(root, path):
            nonlocal paths
            if root is None:
                return None
            if root.left is None and root.right is None:
                paths.append('->'.join(path + [str(root.val)]))
            findPaths(root.left, path + [str(root.val)])
            findPaths(root.right, path + [str(root.val)])
        path = []
        findPaths(root, path)
        return paths
        