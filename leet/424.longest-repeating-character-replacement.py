#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

from collections import Counter

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use this to determine majority char in substring 
        chars = Counter()
        left = right = 0
        res = 0
        while right < len(s):
            chars[s[right]] += 1
            # figure out the count of the most common char in the substring
            # figure out the total scount in the substring
            # subtract these until difference is greater than k

            # print("pre main chars: ", chars)
            # print("pre main l, r: ", left, right)
            common = chars.most_common(1)
            subK = chars.total() - common[0][1]
            while subK > k:
                chars[s[left]] -= 1
                left += 1
                common = chars.most_common(1)
                subK = chars.total() - common[0][1]
                # print("sub k: ", subK)
                # print("sub chars: ", chars)
                # print("sub l, r: ", left, right)

            # print("post main chars: ", chars)
            # print("post main l, r: ", left, right)
            res = max(res, right - left +1)
            right += 1
        return res


        
# @lc code=end

