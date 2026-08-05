class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(row: int, col: int) -> None:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if image[row][col] != start_color:
                return

            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image