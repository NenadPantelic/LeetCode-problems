#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:21:16 2020

@author: nenad
"""
"""
Problem URL: https://leetcode.com/problems/implement-trie-prefix-tree/
Problem description: 
 Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False
        
    def setEnd(self):
        self.isEnd = True
        
    def checkIsEnd(self):
        return self.isEnd
    
    def containsKey(self, key):
        return self.links[ord(key) - ord("a")] is not None
    
    def getNode(self, key):
        return self.links[ord(key) - ord("a")]
    
    def setNode(self, key, node):
        self.links[ord(key)-ord("a")] = node
        
        
   
    

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # empty node
        self.root = TrieNode()
        
    # Time: O(len(word)), space: O(len(word)) - in case we need to insert all of the chars from the word
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        
        for ch in word:
            # key is not present in Trie - insert it into Trie
            if not node.containsKey(ch):
                node.setNode(ch, TrieNode())
            node = node.getNode(ch)
        # mark the last char in the word as ending char in Trie (leaf)
        node.setEnd()
        
    # Time: O(len(word)), space: O(1)    
    def searchPrefix(self, word:str) -> bool:
        node = self.root
        for ch in word:
            # if char is present, go to next char from the word
            if node.containsKey(ch):
                node = node.getNode(ch)
            # else - return None (prefix is not present)
            else:
                return None
        return node
        
    # Time: O(len(word)), space: O(1)    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # return if complete word is in the trie, not as a prefix, but 
        # if the last char of the word is the Trie leaf
        node = self.searchPrefix(word)
        return node is not None and node.checkIsEnd()
        
        
    # Time: O(len(word)), space: O(1)    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.searchPrefix(prefix)
        return node is not None
    
trie = Trie();

trie.insert("apple");
print(trie.search("apple")) # true
print(trie.search("app")) # false
print(trie.startsWith("app")) # true
trie.insert("app")
print(trie.search("app")) # true