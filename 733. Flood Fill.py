class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(x, y, start, p):
            queue = [(x, y, start)]
            X, Y = len(image), len(image[0])
            
            while queue:
                u, v, w = queue.pop(0)
                
                if not vis[u][v]:
                    vis[u][v] = True
                    image[u][v] = p
                    
                    dx = [1, 0, 0, -1]
                    dy = [0, -1, 1, 0]
                    
                    for i in range(4):
                        new_x = u + dx[i]
                        new_y = v + dy[i]
                        
                        if new_x >= 0 and new_y >= 0 and new_x < X and new_y < Y:
                            if not vis[new_x][new_y]:
                                if image[new_x][new_y] == start:
                                    queue.append((new_x, new_y, start))

        vis = [[False for j in range(len(image[0]))] for i in range(len(image))]
        bfs(sr, sc, image[sr][sc], color)
        return image
