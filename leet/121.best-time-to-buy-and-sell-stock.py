#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # build "max after index array used to find the best place to sell for a given point"
        maxes = [0] * len(prices)
        maxes[-1] = prices[-1]
        res = prices[-1] - prices[0]
        i = len(prices)-2
        while i >= 0:
            price = prices[i]
            maxes[i] = max(price, maxes[i+1])
            res = max(res, maxes[i] - prices[i])
            i -= 1
        return max(res, 0)


        
# @lc code=end

