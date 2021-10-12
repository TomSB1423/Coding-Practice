import math
from pprint import pprint


class Solution:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        pprint(self.matrix)

    def rotate(self):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(self.matrix)
        for i in range(math.ceil(n / 2)):
            for j in range(n // 2):
                temp = self.matrix[n - 1 - j][i]
                self.matrix[n - 1 - j][i] = self.matrix[n - 1 - i][n - j - 1]
                self.matrix[n - 1 - i][n - j - 1] = self.matrix[j][n - 1 - i]
                self.matrix[j][n - 1 - i] = self.matrix[i][j]
                self.matrix[i][j] = temp


s = Solution([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
s.rotate()
s.print_matrix()
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
