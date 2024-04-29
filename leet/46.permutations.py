#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        allPerms = []
        for perm in permutations(nums[1:]):
            for i in range(len(nums)):
                allPerms.append(tuple(perm[:i]) + tuple(nums[0:1]) + tuple(perm[i:]))

        return allPerms



        
# @lc code=end

