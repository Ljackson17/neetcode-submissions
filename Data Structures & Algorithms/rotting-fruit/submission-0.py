from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 1. Initial scan
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # 2. If no fresh fruit, it takes 0 minutes
        if fresh == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        # 3. BFS
        while queue and fresh > 0:
            # Process one minute's worth of rotten fruits
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Infect if valid and fresh
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1
