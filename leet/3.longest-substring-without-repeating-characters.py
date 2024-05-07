#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = Counter()
        l, r = 0, 0
        max_no_repeat_length = 0
        while r < len(s):
            rChar = s[r]
            window_chars[rChar] += 1

            while window_chars[rChar] > 1:
                # popping count from l since it's decrementing
                window_chars[s[l]] -= 1
                # going to look at rth char again next itr
                # window_chars[rChar] -= 1
                l += 1

            # only case that the max str can increase
            max_no_repeat_length = max(max_no_repeat_length, r-l+1)
            r += 1

        return  max_no_repeat_length

# @lc code=end

