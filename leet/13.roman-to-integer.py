#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {
                '': 0,
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
        }
        sRev = reversed(s)
        prevChar = ''
        prevValue = 0
        result = 0
        for curChar in sRev:
            currentValue = romanValues[curChar]
            if romanValues[prevChar] > currentValue:
                result += prevValue - currentValue
                prevValue = 0
            else:
                result += prevValue
                prevValue = currentValue
            prevChar = curChar
        result += prevValue
        return result



        
# @lc code=end
