class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # DFS function
        def dfs(r, c):
            # Check boundaries and water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # Mark visited land as water
            grid[r][c] = "0"

            # Visit all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse grid
        for i in range(rows):
            for j in range(cols):
                # Found new island
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count