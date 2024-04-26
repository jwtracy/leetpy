#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Memory limits
        # stack = []
        # cur = head
        # while cur:
        #     stack.append(cur.val)
        # newHead = ListNode()
        # cur = newHead
        # while stack:
        #     cur.next = ListNode(stack.pop())
        #     cur = cur.next
        # return newHead.next

        prev, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
        
# @lc code=end

