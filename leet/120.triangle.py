#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:

    def minimumSubTotal(self, triangle: List[List[int]], depth: int, index: int) -> int:
        # no more children so just return it's value
        if depth == len(triangle) - 1:
            return triangle[depth][index]
        if (depth, index) not in self.subTotals:
            self.subTotals[(depth, index)] = min(triangle[depth][index] + self.minimumSubTotal(triangle, depth + 1, index),
                   triangle[depth][index] + self.minimumSubTotal(triangle, depth + 1, index + 1))
        return self.subTotals[(depth, index)]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #mintotal = min(mintotal(leftTriangle), mintotal(right))
        self.subTotals = {}
        return self.minimumSubTotal(triangle, 0, 0)
        
# @lc code=end
