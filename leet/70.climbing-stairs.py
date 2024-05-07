#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climb(self, i: int, n: int, memo: List[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb(i+1, n, memo) + self.climb(i+2, n, memo)
        return memo[i]
        

    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        return self.climb(0, n, memo)
    
        
# @lc code=end

