#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

from collections import deque

# @lc code=start
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(0, 0)])
        seen = set()
        depth = -1
        while q:
            next = q.popleft()
            if next[0] == amount:
                depth = next[1]
                break
            # is_too_large = True
            for c in coins:
                next_sum = next[0]+c
                # if next_sum <= amount:
                #     is_too_large = False
                if next_sum <= amount and next_sum not in seen:
                    seen.add(next_sum)
                    q.append((next_sum, next[1]+1))

            # if is_too_large:
            #     return -1
        return depth
                
        
# @lc code=end

