#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:38:07 2020

@author: nenad
"""


"""
Problem URL:  https://leetcode.com/problems/symmetric-tree/
Problem description:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

"""

# Definition for a binary tree node.
# Time: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def areTreesMirrored(firstTreeRoot, secondTreeRoot):
            if firstTreeRoot is None and secondTreeRoot is None:
                return True
            
            if not firstTreeRoot or not secondTreeRoot or firstTreeRoot.val != secondTreeRoot.val:
                return False
            return areTreesMirrored(firstTreeRoot.left, secondTreeRoot.right) and \
        areTreesMirrored(firstTreeRoot.right, secondTreeRoot.left)
        return areTreesMirrored(root, root)
    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True
        leftSubTreeQueue, rightSubTreeQueue = [root], [root]
        while leftSubTreeQueue and rightSubTreeQueue:
            nodeFromLeft, nodeFromRight  = leftSubTreeQueue.pop(0), rightSubTreeQueue.pop(0)
            if not nodeFromLeft and not nodeFromRight:
                continue
            if not nodeFromLeft or not nodeFromRight:
                return False
            
            if  nodeFromLeft.val == nodeFromRight.val:
                leftSubTreeQueue.append(nodeFromLeft.left)
                leftSubTreeQueue.append(nodeFromLeft.right)
                
                rightSubTreeQueue.append(nodeFromRight.right)
                rightSubTreeQueue.append(nodeFromRight.left)
            else:
                return False
        return len(leftSubTreeQueue) == len(rightSubTreeQueue) == 0
    def isSymetric(self, root):
        def checkSymetry(left, right):
            if left is right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and checkSymetry(left.right, right.left) \
                and checkSymetry(left.left, right.right)
        if root is None: return True
        return checkSymetry(root.left, root.right)
    
        

sol = Solution()

# Test 1    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(3)

n1.left = n2
n1.right = n3
n2.right = n4
n3.right = n5

           
print(sol.isSymmetric(n1))
        
  
# Test 1    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
n7 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7      
print(sol.isSymmetric(n1))
