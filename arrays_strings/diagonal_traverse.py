"""Diagonal Traverse.

Given an m x n matrix mat, return an array of all the elements of the array in
a diagonal order.
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        lis = []
        diag = []
        rev = 1  # determines whether to reverve list of diagonals
        # get the first half of diagonals
        for n in range(len(mat[0])):
            m = 0
            diag = []
            while n > -1 and m < len(mat):
                diag.append(mat[m][n])
                n -= 1
                m += 1
            if rev < 0:
                lis += diag
            else:
                diag.reverse()
                lis += diag
            rev *= -1

        # get the second half of diagonals
        for m in range(1, len(mat)):
            n = len(mat[0]) - 1
            diag = []
            while m < len(mat) and n > -1:
                diag.append(mat[m][n])
                n -= 1
                m += 1
            if rev < 0:
                lis += diag
            else:
                diag.reverse()
                lis += diag
            rev *= -1

        return lis
