#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        memo = dict()
        for i, n in enumerate(nums):
            memo[n] = i
        for i, n in enumerate(nums):
            complement = memo.get(target - n, i)
            if i != complement:
                return [i, complement]



        
# @lc code=end

