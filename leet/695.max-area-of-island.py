#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int) -> int:
        n, m = len(grid), len(grid[0])
        grid[i][j] = 0
        area = 1
        if i+1 < n and grid[i+1][j] == 1: area += self.dfs(grid, i+1, j)
        if j+1 < m and grid[i][j+1] == 1: area += self.dfs(grid, i, j+1)
        if i-1 >= 0 and grid[i-1][j] == 1: area += self.dfs(grid, i-1, j)
        if j-1 >= 0 and grid[i][j-1] == 1: area += self.dfs(grid, i, j-1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea 
        
# @lc code=end

