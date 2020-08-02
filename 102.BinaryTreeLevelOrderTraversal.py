#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:38:12 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        
        levelNodes = defaultdict(list)
        levelNodes[0] = [root.val]
        level = 0
        queue = deque([(root, 0)])
        while queue:
            nextNode, level = queue.popleft()
            if nextNode.left:
                queue.append((nextNode.left, level+1))
                levelNodes[level+1].append(nextNode.left.val)
            
            if nextNode.right:
                queue.append((nextNode.right, level+1))
                levelNodes[level+1].append(nextNode.right.val)
                
        levelNodesAsMatrix = [levelNodes[level] for level in range(level+1)]
        return levelNodesAsMatrix
            
            
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right=n5

print(Solution().levelOrder(n1))