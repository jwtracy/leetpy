#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # print(self.binarySearch(numbers, 15))
        left, right = 0, len(numbers)-1
        while left <= right:
            partial_sum = numbers[left] + numbers[right]
            if partial_sum == target:
                return [left+1, right+1]
            elif partial_sum < target:
                left += 1
            else:
                right -= 1
        return []

        
# @lc code=end

