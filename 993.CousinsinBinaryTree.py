#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:19:47 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/cousins-in-binary-tree/
Problem description: 
Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


"""
# Time: O(n), space: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # values of nodes are unique - there is no overwritting issue, so we can use maps
    def __init__(self):
        self.depths = {}
        self.parents = {}
    
    def DFS(self, root, parent = None, counter = 0):
        if root is None:
            return
        # add depth value of this node
        self.depths[root.val] = counter
        # add record about parent of this node
        self.parents[root.val] = parent
        # check left and right subtree
        self.DFS(root.left, root, counter+1)
        self.DFS(root.right, root, counter+1)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.depths = {}
        self.parents = {}
        self.DFS(root)
        # check if depths are the same and if they don't have the same parent
        return self.depths[x] == self.depths[y] and \
            self.parents[x] != self.parents[y]

sol = Solution()

# Test 1

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4

print(sol.isCousins(n1, 4, 3))


# Test 2

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.right = n4
n3.right = n5

print(sol.isCousins(n1, 4, 5))



# Test 3

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.right = n4

print(sol.isCousins(n1, 2, 3))
