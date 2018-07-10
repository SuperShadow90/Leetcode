import Queue
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
                    self.bfs(i,j,visited)
                    count += 1
        return count
                        
    def bfs(self, i, j, visited):
        visited[i][j] = True
        queue = Queue.Queue()
        queue.put((i,j))
        while not queue.empty():
            i, j = queue.get()
            self.addToQueue(i, j+1, queue, visited)
            self.addToQueue(i, j-1, queue, visited)
            self.addToQueue(i+1, j, queue, visited)
            self.addToQueue(i-1, j, queue, visited)
                
                
    def addToQueue(self, x, y, queue, visited):
        if x >= 0 and y >= 0 and x < self.row_num and y < self.col_num and not visited[x][y] and self.grid[x][y] == '1':
            visited[x][y] = True
