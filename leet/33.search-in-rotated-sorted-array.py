#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        k = 0
        while left < right:
            mid = left + (right - left) // 2
            # print("l, m, r: ", left, mid, right)
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid+1
            else:
                k = left
                break
        k = left
        left, right = k, len(nums) - 1 + k
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid%len(nums)] == target:
                return mid%len(nums)
            elif nums[mid%len(nums)] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

            


        
# @lc code=end

