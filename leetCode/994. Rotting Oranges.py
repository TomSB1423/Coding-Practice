class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # create queue for rotten oranges to start
        queue = []
        # Count for no. minutes
        minutes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j, minutes])

        while queue:
            # remove and return first in array
            i, j, minutes = queue.pop(0)
            # change adjecent to rotten in fresh
            changed = self.check_surrounding(grid, i, j, queue, minutes)

        # check if no fresh oranges left
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes

    # turns adjacent fresh -> rotten
    def check_surrounding(self, grid, i, j, queue, minutes):
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            grid[i][j+1] = 2
            queue.append([i, j+1, minutes + 1])
        if j-1 >= 0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
            queue.append([i, j-1, minutes + 1])
        if i+1 < len(grid) and grid[i+1][j] == 1:
            grid[i+1][j] = 2
            queue.append([i+1, j, minutes + 1])
        if i-1 >= 0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
            queue.append([i-1, j, minutes + 1])
        return
