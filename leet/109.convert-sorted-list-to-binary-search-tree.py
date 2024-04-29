#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # get to the point of half the list and the whole list
        first = head
        half, halfPrev = first, None
        cur = first
        cntr = 0
        while cur:
            if cntr % 2 == 1:
                halfPrev = half
                half = half.next
            cur = cur.next
            cntr += 1

        root = None
        if cntr >= 3:
            halfPrev.next = None
            root = TreeNode(half.val)
            root.left = self.sortedListToBST(first)
            root.right = self.sortedListToBST(half.next)
        elif cntr == 1:
            root = TreeNode(half.val)
        elif cntr < 3:
            root = TreeNode(half.val)
            root.left = TreeNode(first.val)

        return root
    
        # rotate about the middle of the tree 

        
# @lc code=end

