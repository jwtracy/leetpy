#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of cols
        # target is out of the range of the matrix
        if target > matrix[m - 1][-1]:
            return False
        elif target < matrix[0][0]:
            return False

        # find correct row in binary search
        l, i, r = 0, m//2, m-1
        while l <= r:
            first, last = matrix[i][0], matrix[i][-1]
            # print(first, last)
            # print("l, i, r: ", l, i, r)
            if target >= first and target <= last:
                break
            elif target < first:
                # look in smaller half
                r = i - 1
            elif target > last:
                l = i + 1

            # mid is now new mid
            i = l + (r - l) // 2
                
        # print("final: l, i, r: ", l, i, r)
        
        # find correct row in binary search
        l, j, r = 0, n//2, n-1
        while l <= r:
            num = matrix[i][j]
            # print("l, j, r: ", l, j, r)
            if target == num:
                return True
            elif target < num:
                # look in smaller half
                r = j - 1
            elif target > num:
                l = j + 1

            # mid is now new mid
            j = l + (r - l) // 2

        # print("final: l, j, r: ", l, j, r)

        return False

        

        # find exact column

        
# @lc code=end

