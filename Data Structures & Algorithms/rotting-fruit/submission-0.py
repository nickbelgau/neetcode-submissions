class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_fruit = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue and fresh_fruit:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    next_row = row + row_change
                    next_col = col + col_change

                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        fresh_fruit -= 1
                        queue.append((next_row, next_col))

            minutes += 1

        return minutes if fresh_fruit == 0 else -1
        