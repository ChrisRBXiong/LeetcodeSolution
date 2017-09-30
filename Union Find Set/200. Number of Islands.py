"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
11110
11010
11000
00000
Answer: 1
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.visited = [[0  for j in range(len(grid[0]))] for i in range(len(grid))]
        self.grid = grid
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if self.grid[x][y] == '1' and not self.visited[x][y]:
                    count += 1
                    self.dfs(x, y)
                    print(self.visited)
        return count
    
    def dfs(self, x, y):
        dx, dy = (0, 0, -1, 1), (-1, 1, 0, 0)
        for d in range(4):
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < len(self.grid) and 0 <= ty < len(self.grid[0]):
                if self.grid[tx][ty] == '1' and not self.visited[tx][ty]:
                    self.visited[tx][ty] = 1
                    self.dfs(tx, ty)
        

            
            