#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfsSided(root: TreeNode, leftFirst: bool) -> list:
            if not root:
                return [101]
            if leftFirst:
                return [root.val] + dfsSided(root.left, leftFirst) + dfsSided(root.right, leftFirst)
            else:
                return [root.val] + dfsSided(root.right, leftFirst) + dfsSided(root.left, leftFirst)

        left_stack, right_stack = dfsSided(root, True), dfsSided(root, False)
        if len(left_stack) != len(right_stack):
            return False
        
        for i in range(len(left_stack)):
            if left_stack.pop() != right_stack.pop():
                return False
        
        return True


# @lc code=end

