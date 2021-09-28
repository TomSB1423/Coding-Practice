class Solution:
    def numIslands(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])

        def helper(r, c):
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i < 0 or j < 0 or i >= n_rows or j >= n_cols:
                        continue
                    if (i == r + 1 and j == c + 1) or (i == r - 1 and j == c - 1) or (i == r - 1 and j == c + 1) or (i == r + 1 and j == c - 1):
                        continue
                    if grid[i][j] == "1":
                        grid[i][j] = "2"
                        helper(i, j)

        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "2"
                    helper(i, j)
        return count


class Solution:
    def numIslands(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])

        def helper(i, j):
            if i < 0 or j < 0 or i >= n_rows or j >= n_cols or grid[i][j] != "1":
                return
            grid[i][j] = "2"
            helper(i+1, j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i, j-1)

        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    count += 1
                    helper(i, j)
        return count
