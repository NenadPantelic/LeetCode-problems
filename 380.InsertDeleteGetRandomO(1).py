#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:27:01 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/insert-delete-getrandom-o1/
Problem description: 
Insert Delete GetRandom O(1)
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

# Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

# Returns false as 2 does not exist in the set.
randomSet.remove(2);

# Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

# getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

# Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

# 2 was already in the set, so return false.
randomSet.insert(2);

# Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

"""
from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        retVal = True if val not in self.map else False
        if retVal:
            self.map[val] = len(self.arr)
            self.arr.append(val)
        return retVal

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        retVal = True if val in self.map else False
        if retVal:
            index = self.map.pop(val)
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.arr.pop(-1)
            if len(self.arr) > 0 and index < len(self.arr):
                self.map[self.arr[index]] = index
            

        return retVal
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        count = len(self.arr)
        return self.arr[randint(0, count-1)]

    

# Init an empty set.
randomSet = RandomizedSet();

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

# Returns false as 2 does not exist in the set.
randomSet.remove(2);

# Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

# getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

# Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

# 2 was already in the set, so return false.
randomSet.insert(2);

# Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
        