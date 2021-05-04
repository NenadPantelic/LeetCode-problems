#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:07:30 2021

@author: nenad
"""

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
        
#         wordList.append(beginWord)
#         n = len(wordList)
#         graph = defaultdict(list)
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 if self._isDistEqOne(wordList[i], wordList[j]):
#                     graph[wordList[i]].append((wordList[j], 1))
#         if len(graph[beginWord]) == 0 or len(graph[endWord]) == 0:
#             return 0
#         dist = self.shortestPath(beginWord, graph)
#         return dist[endWord] + 1 if dist[endWord] != float("inf") else 0
        
    
#     def shortestPath(self, source, graph):
#         pq = []
#         #print(graph)
#         visited = {word: False for word in graph}
#         dist = {word: float("inf") for word in graph}
#         heappush(pq, (0, source))
#         while len(pq):
#             #print(pq)
#             #print(dist)
#             distance, curr_node = heappop(pq)
#             #print(curr_node, distance)
#             visited[curr_node] = True
#             #print(visited)
#             for node, distanceFromCurrNode in graph[curr_node]:
#                 newDist = dist[node]
#                 if visited[node]:
#                     continue
#                 if distance + distanceFromCurrNode < dist[node]:
#                     newDist = distance + distanceFromCurrNode 
#                 dist[node] = newDist
#                 heappush(pq, (newDist, node))
#         return dist
                
        
#     def _distBetweenWords(self, word1, word2):
#         dist = 0
#         m, n = len(word1), len(word2)
#         for i in range(min(m, n)):
#             if word1[i] != word2[i]:
#                 dist += 1

#         return dist + max(m, n) - i - 1
    
#     def _isDistEqOne(self, word1, word2):
#         return self._distBetweenWords(word1, word2) == 1
#         return self._distBetweenWords(word1, word2) == 1

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        wordChars = set("".join(word for word in wordList))
        deq = deque()
        deq.append((beginWord, 1))
        while len(deq):
            word, length = deq.popleft()
            for i in range(len(word)):
                for char in wordChars:
                    newWord = word[:i] + char + word[i+1:]
                    if newWord  == endWord:
                        return length + 1
                    if newWord in wordList:
                        wordList.remove(newWord)
                        deq.append((newWord, length+1))
                    
        return 0
        
    
wordList = ["hot","dot","dog","lot","log","cog"]
wordList = ["hot","dot","dog","lot","log"]
wordList = ["hat","het","her","cer","cor", "cog"]
wordList = ["hot","dog"]
#print(Solution().ladderLength("hit", "cog", wordList))
print(Solution().ladderLength("hot", "dog", wordList))
#print(Solution()._distBetweenWords("hort", "dot"))