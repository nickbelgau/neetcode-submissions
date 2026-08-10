class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # confirm grid is open "0" at first position
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 0)])
        grid[0][0] = 1 # temporarily mark first cell as unvisited 
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
            row, col, moves = queue.popleft()
            # pop to remove the last move, and save the values for testing

            if row == n - 1 and col == n - 1:
                return moves + 1

            for row_change, col_change in directions:
                # the loop explores all directions
                next_row = row + row_change
                next_col = col + col_change

                if (
                    0 <= next_row < n
                    and 0 <= next_col < n # ensures move is within boundaries
                    and grid[next_row][next_col] == 0 # ensures next cell is open
                ):
                    # the valid next cell gets marked as "1"
                    grid[next_row][next_col] = 1 
                    queue.append((next_row, next_col, moves + 1))

        return -1