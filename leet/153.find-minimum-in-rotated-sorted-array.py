#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            print("l, m, r: ", left, mid, right)
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid+1
            else:
                return nums[left]
        return nums[left]
            

# @lc code=end

