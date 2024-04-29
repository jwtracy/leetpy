#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # build sets of subgrids as you go
        rows = {x: set() for x in range(10)}
        cols = {x: set() for x in range(10)}
        subs = {x: set() for x in range(10)}
        for row in range(len(board)):
            for col in range(len(board[row])):
                digit = board[row][col]
                sub = row // 3 * 3 + col // 3
                # print("rows: ", rows) 
                # print("cols: ", cols) 
                # print("subs: ", subs)
                # print()
                if (digit != "." and
                    (digit in rows[row]
                    or digit in cols[col]
                    or digit in subs[sub])):
                    return False
                else:
                    rows[row].add(digit)
                    cols[col].add(digit)
                    subs[sub].add(digit)
        return True


                
                



        
        
# @lc code=end

