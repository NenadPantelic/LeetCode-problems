#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:57:27 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/search-in-a-binary-search-tree/
Problem description: 
 Search in a Binary Search Tree
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Time: O(height of BST), space: O(1) -> implicitly O(height) - usage of stack (recursion calls)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        
        # val is less than root value - go to the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)
        # val is greater than root value - go to the right subtree
        if root.val < val:
            return self.searchBST(root.right, val)
        return root
    

sol = Solution()

# Test 1
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)     

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

node = sol.searchBST(n1, 2)
print(node.val if node else None)

node = sol.searchBST(n1, 5)
print(node.val if node else None)