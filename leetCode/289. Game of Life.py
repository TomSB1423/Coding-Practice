class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 | 0 | 0
        # 1 | 0 | 1
        # 0 | 1 | 2
        # 1 | 1 | 3
        n_row = len(board)
        n_col = len(board[0])

        def count_board(row, col):
            count = 0
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if (i == row and j == col) or i < 0 or j < 0 or i >= n_row or j >= n_col:
                        continue
                    if board[i][j] in [1, 3]:
                        count += 1
            return count

        for i in range(n_row):
            for j in range(n_col):
                count = count_board(i, j)
                if board[i][j] == 1:
                    if count in [2, 3]:
                        board[i][j] = 3
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1
        return board


s = Solution()
print(s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
