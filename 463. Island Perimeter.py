class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def bfs(x, y, c):
            X, Y = len(grid), len(grid[0])
            queue = [(x, y)]

            while queue:
                u, v = queue.pop(0)

                if not visited[u][v]:
                    visited[u][v] = True

                    dx = [1, 0, 0, -1]
                    dy = [0, 1, -1, 0]

                    for i in range(4):
                        new_x, new_y = u + dx[i], v + dy[i]
                        if new_x >= 0 and new_x < X and new_y >= 0 and new_y < Y:
                            if not visited[new_x][new_y]:
                                if grid[new_x][new_y] == 1:
                                    queue.append((new_x, new_y))
                                else:
                                    c += 1
                        else:
                            c += 1
            return c
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs(i, j, 0)
                    break


