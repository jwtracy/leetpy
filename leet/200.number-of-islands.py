#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

from collections import deque

# @lc code=start
class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        n, m = len(grid), len(grid[0])
        grid[i][j] = '0'
        if i+1 < n and grid[i+1][j] == '1': self.dfs(grid, i+1, j)
        if j+1 < m and grid[i][j+1] == '1': self.dfs(grid, i, j+1)
        if i-1 >= 0 and grid[i-1][j] == '1': self.dfs(grid, i-1, j)
        if j-1 >= 0 and grid[i][j-1] == '1': self.dfs(grid, i, j-1)
        pass

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1
                    self.dfs(grid, i, j)
        return count



            

                    

# @lc code=end

