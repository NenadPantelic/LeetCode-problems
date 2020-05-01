#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:04:00 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Problem description: 

Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
  
    
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# For every node, we have the following cases of sum path:
# Path involves:
# a) current node only
# b) left child and current node
# c) right child and current node
# d) left child + current node + right child

# Time: O(n), space: implicitly O(n) -  n calls of recursive function -> O(n) on stack

class Solution:
    def __init__(self):
        self.result = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float("-inf")
        self.maxPathSumUtil(root)
        return self.result
    def maxPathSumUtil(self, root):
        # default case - root is None (no path to make)
        if root is None:
            return 0
        # examine both subtrees - left and right
        leftChildPathSum = self.maxPathSumUtil(root.left)
        rightChildPathSum = self.maxPathSumUtil(root.right)
        
        # decide where we will go, via left child subtree or righ child subtree or we will not go with child nodes
        # at all -> we examined cases a,b,c
        maxChildPath = max(max(leftChildPathSum, rightChildPathSum) + root.val, root.val)
        # examine case d) -> is it better to go leftCh -> root -> rightChild
        # we're acumulating the best result in self.result, but retutrn maxChildPath (this is utilitty function
        # )  that returns max path sum from this node as root (not the max path sum in the whole tree)
        maxOfAllPathsThroughThisNode = max(maxChildPath, leftChildPathSum + rightChildPathSum + root.val)
        self.result = max(self.result, maxOfAllPathsThroughThisNode)
        return maxChildPath
    
sol = Solution()

# Test 1
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)   
node1.left = node2
node1.right = node3
print(sol.maxPathSum(node1))


# Test 2
node1 = TreeNode(-10)
node2 = TreeNode(9)
node3 = TreeNode(20) 
node4 = TreeNode(15)
node5 = TreeNode(7)  
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
print(sol.maxPathSum(node1))
