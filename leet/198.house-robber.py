#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob_best(self, nums: List[int], i: int,  memo: List[int]):
        if memo[i] >= 0:
            return memo[i]
        if i == len(nums) - 1:
            memo[i] = nums[i]
        elif i == len(nums) - 2:
            memo[i] = max(nums[i], nums[i+1])
        else:
            memo[i] = max(nums[i] + self.rob_best(nums, i+2, memo), self.rob_best(nums, i+1, memo))
        return memo[i]

    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.rob_best(nums, 0, memo)
        
# @lc code=end

