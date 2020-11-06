#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:46:27 2020

@author: nenad
"""

"""

Problem URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Problem description: 
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict
# Time and space: O(n)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []
        levelsMap = defaultdict(list)
        queue = [(root, 0)]
        level = 0
        #levelsMap[level].append(root)
        
        while queue:
            node, level = queue.pop(0)
            if level % 2 == 0:
                levelsMap[level].append(node.val)
            else:
                levelsMap[level].insert(0, node.val)
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        
        
        return list(levelsMap.values())

sol = Solution()

# Test 1    
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print(sol.zigzagLevelOrder(n1))
            