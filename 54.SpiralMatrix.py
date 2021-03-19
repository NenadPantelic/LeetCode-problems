"""
URL: https://leetcode.com/problems/spiral-matrix/
Description:
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = 0,0
        result = []
        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        firstRow, lastRow =  0, m-1
        firstCol, lastCol = 0,  n-1
        while firstRow <= lastRow and firstCol <= lastCol:
            for i in range(firstCol, lastCol + 1): 
               result.append(matrix[firstRow][i])
            firstRow += 1 
            if firstRow > lastRow: break
            for i in range(firstRow, lastRow + 1):
                result.append(matrix[i][lastCol])
            lastCol -= 1
            if lastCol < firstCol: break
            for i in range(lastCol, firstCol - 1, -1):
                result.append(matrix[lastRow][i])
            lastRow -= 1
            if lastRow < firstRow: break
            for i in range(lastRow, firstRow-1, -1):
                result.append(matrix[i][firstCol])
            firstCol += 1

        return result
