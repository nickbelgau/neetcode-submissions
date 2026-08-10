class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        )

        while queue:
            row, col, length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change

                if (
                    0 <= next_row < n
                    and 0 <= next_col < n
                    and grid[next_row][next_col] == 0
                ):
                    grid[next_row][next_col] = 1
                    queue.append((next_row, next_col, length + 1))

        return -1