class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        self.grid = grid
        self.row_num = len(grid)
        self.col_num = len(grid[0])
        visited = [[False for _ in range(self.col_num)] for _ in range(self.row_num)]
        count = 0
    
        for i in range(self.row_num):
            for j in range(self.col_num):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i,j,visited)
                    count += 1
        return count
                        
    def dfs(self, i, j, visited):
        if i < 0 or j < 0 or i >= self.row_num or j >= self.col_num or visited[i][j]:
            return 
        visited[i][j] = True
        if self.grid[i][j] == "1":
            self.dfs(i+1, j, visited)
            self.dfs(i-1, j, visited)
            self.dfs(i, j+1, visited)
            self.dfs(i, j-1, visited)