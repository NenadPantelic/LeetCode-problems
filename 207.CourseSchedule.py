#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:37:56 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/course-schedule/
Problem description: 
Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
   Hide Hint #1  
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
   Hide Hint #2  
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
   Hide Hint #3  
Topological sort could also be done via BFS.

"""
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = defaultdict(list)
        # create adj. list
        for pair in prerequisites:
            # prerequisite -> course
            graph[pair[1]].append(pair[0])
        visited = [False] * numCourses
        #stack = []
        def topsort(node, previousNodes = set()):
            visited[node] = True
            previousNodes.add(node)

            
            for neighbour in graph[node]:
                # cycle detected
                if neighbour in previousNodes:
                    return False
                # node already examined in top sort
                if visited[neighbour]:
                    continue
                # repeat topsort for current node's neighbours
                res = topsort(neighbour, previousNodes)
                # if cycle detected - return False
                if not res:
                    return res
            # backtrack - all neighbours examined
            previousNodes.remove(node)    
            return True
                
        # check every node - check if cycle is detected in topological sort (ordering)
        for i in range(numCourses):
            if visited[i]: continue
            res = topsort(i)
            if not res:
                return False
        return True

        

sol = Solution()

# Test 1
numCourses = 2; prerequisites = [[1,0]]
print(sol.canFinish(numCourses, prerequisites))

# Test 2
numCourses = 2; prerequisites = [[1,0], [0,1]]
print(sol.canFinish(numCourses, prerequisites))

# Test 3
numCourses = 3; prerequisites = [[1,0],[0,2],[2,1]]
print(sol.canFinish(numCourses, prerequisites))

# Test 4
numCourses = 4; prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
print(sol.canFinish(numCourses, prerequisites))

# Test 5
numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.canFinish(numCourses, prerequisites))