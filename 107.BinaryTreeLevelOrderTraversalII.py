#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 00:02:10 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Problem description: 
Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""
# Time: O(n), space: O(n)
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        visited = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        levelCounter = 0
        while queue:
            nextNode, level = queue.popleft()
            visited[level].append(nextNode.val)
            if nextNode.left: queue.append((nextNode.left, level+1))
            if nextNode.right: queue.append((nextNode.right, level+1))
        maxLevel = level
        levels = []    
        while maxLevel >= 0:
            levels.append(visited[maxLevel])
            maxLevel -= 1
        return levels
        
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
print(sol.levelOrderBottom(n1))
