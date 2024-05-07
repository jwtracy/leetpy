#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:

        solutions = []
        memo = dict()
        for i, n in list(enumerate(nums))[start:]:
            memo[n] = i
        for i, n in list(enumerate(nums))[start:]:
            complement = memo.get(target - n, i)
            if i != complement and i < complement:
                solutions.append([i, complement])
        return solutions

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i, n in enumerate
        
# @lc code=end

