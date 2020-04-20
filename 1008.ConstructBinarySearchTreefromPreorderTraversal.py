#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:04:36 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Problem description:
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Note: 

1 <= preorder.length <= 100
The values

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Time: O(n), space: O(n)
class Solution:
    index = 0
    def bstFromPreorder(self, preorder) -> TreeNode:
        n = len(preorder)
        def reconstructBST(minimum, maximum):
            # all elements from preorder are used
            if Solution.index >= n:
                return 
            root = None
            # take next element from preorder array
            nodeValue = preorder[Solution.index]
            # node belongs to the current subtree
            if minimum < nodeValue < maximum:
                # create new node
                root = TreeNode(nodeValue)
                # go to next index
                Solution.index += 1
                if Solution.index < n: 
                    # reconstruct left and right subtree
                    # maximum value in the left subtree will be value of current node (all values in left subtree are smaller)
                    # minimum value in the right subtree will be value of current node (all values in right subtree are greater)
                    root.left = reconstructBST(minimum, nodeValue)
                    root.right = reconstructBST(nodeValue, maximum)
            return root
        # initial bounds are - -oo and +oo
        root = reconstructBST(float("-inf"), float("inf"))
        # reset index - for test cases sake
        Solution.index = 0
        return root
                
    
def preorder(root):
    if root is None:
        return 
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
    
    
sol = Solution()
# Test 1
root = sol.bstFromPreorder([8,5,1,7,10,12])
preorder(root)
            