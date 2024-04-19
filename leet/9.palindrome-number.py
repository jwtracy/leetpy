
#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from collections import deque
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        digits = deque()
        for digit in xStr:
            digits.append(digit)
        
        for i in range(len(digits) // 2):
            if digits.popleft() != digits.pop():
                return False

        return True
        
# @lc code=end

