class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        def set_zero(r, c):
            for i in range(n_rows):
                if matrix[i][c] != 0:
                    matrix[i][c] = "#"
            for i in range(n_cols):
                if matrix[r][i] != 0:
                    matrix[r][i] = "#"

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = "#"
                    set_zero(i, j)

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
