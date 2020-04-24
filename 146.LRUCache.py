#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:51:15 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/lru-cache/
Problem description: 
LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""
# My post on LeetCode - https://leetcode.com/problems/lru-cache/discuss/595379/Python-solution-with-dictionary-and-Linked-List-time-complexity-O(1)-space-complexity-O(n)

# Time: O(1), space: O(n)
# Explanation:
# Every element in cache has the following structure:
# key: [value, previous, next] 
# Generally, I used LL in cache -> first element of the LL (head) is the least recenlty used element, and the tail
# is the most recently used element. So, in case:
# cache.put(1,1) ---> 1 -> None ; map = {1:[1, None, None]}
# cache.put(2,2) ---> 1 -> 2 -> None; map = {1:[1, None, 2], 2:[2, 1, None]}
# cache.put(3,3) ---> 1 -> 2 -> 3 -> None; map = {1:[1, None, 2], 2:[2, 1, 3], 3:[3, 2, None]}
# cache.get(2) ---> 1 -> 3 -> 2 -> None (so, when we use some element (put/get), we move that element to the end of the list - put it at tail)
# map = {1:[1, None, 2], 3:[3, 1, 2], 2:[2, 3, None]}
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}  
        
    # private methods
    # move element to tail position
    # we have three cases - 
    #  a) we're moving head element
    #  b) we're moving tail element - do nothing
    #  c) we're moving internal element - some element between head and tail
    def _moveToTail(self, key):
        # tail element - already at tail (case b)
        if key == self.tail:
            return
        value, previous, next = self.cache[key]
        # we're moving head element - case a)
        if key == self.head:
            # set next element as new head
            self.cache[next][1] = None
            self.head = next
        
        # we're moving interal element
        else:
            # connect previous and next of the current node (case c)
            # before: prev -> key -> next
            # after: prev -> next
            self.cache[previous][2] = next
            # prev <- next
            self.cache[next][1] = previous
        
        # set key after tail in linked list: tail -> key
        self.cache[self.tail][2] = key
        # tail <- key
        self.cache[key][1] = self.tail
        self.cache[key][2] = None
        # key = tail
        self.tail = key
    
    
    # add key to cache - at the end of the linked list        
    def _insert(self, key, value):
        if len(self.cache) == 0:
            self.head = key
        # set new value at the end of ll
        self.cache[key] = [value, self.tail, None]
        if self.tail is not None:
            self.cache[self.tail][2] = key
        # this is new tail
        self.tail = key
    # remove head element - least recently used value
    def _removeHead(self):
        if self.head is not None:
            # get next head
            next = self.cache[self.head][2]
            # if next is not None - set next as new head
            if next is not None:
                self.cache[next][1] = None
            # else - head and tail are the same nodes
            else:
                self.tail = None
            # remove head
            self.cache.pop(self.head)
           # set new head
            self.head = next
            


    def get(self, key: int) -> int:
        # key is not present
        if key not in self.cache:
            return -1
        #value = self.cache[key][0]
        self._moveToTail(key)
        return self.cache[key][0]
    

            
    # Two cases:
    # 1) key is in cache - update cache[key], move key to the end of the LL
    # 2) key is not in cache:
    # a) size is < capacity -> add element in cache, at the end of LL
    # b) size is >= capacity -> remove head element from cache data, add new element at the end
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            self._moveToTail(key)

        else:
            if len(self.cache) < self.capacity:
                # add element to cache                        
                self._insert(key, value)
            else:
                # remove head node and add new element
                self._removeHead()
                self._insert(key, value)
 

            
# cache =LRUCache(2);
# # Test 1
# cache.put(1, 1);
# cache.put(2, 2);
# print(cache.get(1));       #// returns 1
# cache.put(3, 3);    #// evicts key 2
# print(cache.get(2));       ##// returns -1 (not found)
# cache.put(4, 4);    #// evicts key 1
# print(cache.get(1));       #// returns -1 (not found)
# print(cache.get(3));       #// returns 3
# print(cache.get(4));       #// returns 4

# #cache.cache.clear()

# Test 2
# cache = LRUCache(1)
# cache.put(2,1)
# print(cache.get(2))
# cache.put(3,2)
# print(cache.get(2))
# print(cache.get(3))

ops = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
params = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
def parseInput(ops, params):
    cache = LRUCache(params[0][0])
    for i in range(1, len(ops)):
        if ops[i] == "put":
            cache.put(params[i][0], params[i][1])
            #print("OK")
        else:
            #print(cache.get(params[i][0]))
            pass
        print(i)
        #print(cache.cache)
    print(cache.cache)
            
print()
parseInput(ops, params)

