#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:08:47 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Problem description: 
Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

   Hide Hint #1  
Try to utilize the property of a BST.
   Hide Hint #2  
Try in-order traversal. (Credits to @chan13)
   Hide Hint #3  
What if you could modify the BST node's structure?
   Hide Hint #4  
The optimal runtime complexity is O(height of BST).

"""
# Time: O(height + k), space: O(height + k)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nodeCount = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.nodeCount = 0
        def inorder(root):
            if not root: return None
            leftRetVal = inorder(root.left)
            # when we get non-None value, that means we reached the kth element
            if leftRetVal is not None:
                return leftRetVal
            self.nodeCount += 1
            if self.nodeCount == k: return root.val
            # when we get non-None value, that means we reached the kth element
            rightRetVal = inorder(root.right) 
            if rightRetVal is not None:
                return rightRetVal
            
        return inorder(root)
    
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node is None:
                return 
            
            result = inorder(node.left)
            if result is not None: return result
            self.nodeCount += 1
            if self.nodeCount == k:return node.val
            result = inorder(node.right)
            if result is not None: return result
        return inorder(root)
            
            
sol = Solution()

# Test 1
# n1 = TreeNode(3)
# n2 = TreeNode(1)
# n3 = TreeNode(4)
# n4 = TreeNode(2)

# n1.left = n2
# n1.right = n3
# n2.right = n4

# print(sol.kthSmallest(n1, 1))


# Test 1
n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6

print(sol.kthSmallest(n1, 3))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodeCount = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node is None:
                return 
            result = inorder(node.left)
            if result is not None: return result
            self.nodeCount += 1
            if self.nodeCount == k:return node.val
            result = inorder(node.right)
            if result is not None: return result
        return inorder(root)
    
    
class Solution:
	# @type of root: TreeNode
	# @type of k: integer
	# @return type: TreeNode
    count = 0
    def kthSmallest(self, root: TreeNode, k: int) -> TreeNode:
        # write your awesome code here
        Solution.count = 0
        def inorderUtils(root, k):
            if root is None:
                return 
            value = inorderUtils(root.left,k)
            if value is not None:
                return value
            Solution.count += 1
            if k == Solution.count:
                return root.val
            value = inorderUtils(root.right, k)
            if value is not None:
                return value
        #kthVal = None
       	return inorderUtils(root, k)
