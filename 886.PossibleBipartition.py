#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:33:06 2020

@author: nenad
"""

"""

Problem URL: https://leetcode.com/problems/possible-bipartition/
Problem description: 
Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

"""
    
# Time: O(N), space: O(2*N)
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        graph = defaultdict(list)
        # undirected graph
        for a, b  in dislikes:
            #a, b = dislike
            graph[a].append(b)
            graph[b].append(a)
        # every element in dislikes should belong to one or another set - 0 or 1
        nodes = {}
        def putNodeInGroup(node, groupNo = 0):
            # node already visited - check if it belongs to the group we're trying to assign to
            # if not - that's conflict
            if node in nodes:
                return nodes[node] == groupNo
            # assign node to this group
            nodes[node] = groupNo
            # assign group to nodes that current node dislikes
            for neighbour in graph[node]:
                result = putNodeInGroup(neighbour, 1-groupNo) #or groupNo ^ 1
                # there is conflict in group asssigning
                if not result:
                    return False
            return True
        # assign every node to some group
        for node in graph:
            if node in nodes: continue
            if putNodeInGroup(node) == False:
                return False
        return True
        
sol = Solution()

# Test 1
N = 4; dislikes = [[1,2],[1,3],[2,4]]
print(sol.possibleBipartition(N, dislikes))


# Test 2
N = 3; dislikes = [[1,2],[1,3],[2,3]]
print(sol.possibleBipartition(N, dislikes))

# Test 3
N = 5; dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(sol.possibleBipartition(N, dislikes))

# Test 4
N = 10
dislikes = [[4,7],[4,8],[2,8],[8,9],[1,6],[5,8],[1,2],[6,7],[3,10],[8,10],[1,5],[7,10],[1,10],[3,5],[3,6],[1,4],[3,9],[2,3],[1,9],[7,9],[2,7],[6,8],[5,7],[3,4]]
print(sol.possibleBipartition(N, dislikes))
