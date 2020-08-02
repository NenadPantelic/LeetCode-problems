#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:07:50 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/validate-binary-search-tree/
Problem description: 
98. Validate Binary Search Tree
Medium

4054

542

Add to List

Share
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def checkNode(node, minVal = float("-inf"), maxVal = float("inf")):
            if node is None:
                return True
            
            return minVal < node.val < maxVal and checkNode(node.left, minVal, node.val) and \
                checkNode(node.right, node.val, maxVal)
                
        return checkNode(root)
    
sol = Solution()

n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(6)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(sol.isValidBST(n1))

n3.val = 7
n4.val = 6
n5.val = 8
print(sol.isValidBST(n1))



n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(15)
n4 = TreeNode(6)
n5 = TreeNode(20)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print(sol.isValidBST(n1))


