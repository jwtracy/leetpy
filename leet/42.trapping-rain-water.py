#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        volumetric_grid = height.copy()
        left_max = 0
        for i in range(len(height)):
            left_max = max(left_max, height[i])
            volumetric_grid[i] = left_max

        water = 0
        right_max = 0
        for i in range(len(height)):
            elevation = height[len(height) - (i + 1)]
            right_max = max(right_max, elevation)
            if volumetric_grid[len(height) - (i + 1)] > right_max:
                volumetric_grid[len(height) - (i + 1)] = right_max
            water += volumetric_grid[len(height) - (i + 1)] - height[len(height) - (i + 1)]

        return water



            
        
# @lc code=end

