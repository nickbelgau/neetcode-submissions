class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacle_grid = obstacleGrid
        rows = len(obstacle_grid)
        cols = len(obstacle_grid[0])
        cache: dict[tuple[int, int], int] = {}

        def dfs(row: int, col: int) -> int:
            if row >= rows or col >= cols:
                return 0
            if obstacle_grid[row][col] == 1:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1
            if (row, col) in cache:
                return cache[(row, col)]

            cache[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)
            return cache[(row, col)]

        return dfs(0, 0)