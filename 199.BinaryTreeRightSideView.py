#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:44:32 2021

@author: nenad
"""


"""
URL: https://leetcode.com/problems/binary-tree-right-side-view/
Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""



from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 0)]
        while len(queue):
            node, level = queue.pop(0)
            levels[level].append(node.val)
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        # take the rightmost node at every level
        return [levels[i][-1] for i in range(level+1)]