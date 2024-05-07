#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(sanitized)-1
        while left < right:
            if sanitized[left] != sanitized[right]:
                return False
            left += 1
            right -= 1
        return True

        
# @lc code=end

