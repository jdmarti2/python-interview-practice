"""Rotate n x n 2D matrix 90 degrees.

Task: You are given an n x n 2D matrix representing an image, rotate the image
by 90 degrees (clockwise). You have to rotate the image in-place, which means
you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # notice change in coordinates pattern
        # hash map old values in matrix
        old_values = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                old_values[(i, j)] = matrix[i][j]
        # transform matrix using values in old_values
        for a in range(len(matrix)):
            for b in range(len(matrix)):
                matrix[a][b] = old_values[(len(matrix) - (b+1), a)]
