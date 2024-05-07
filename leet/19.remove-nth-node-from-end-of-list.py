#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        nthLastIndex = len(stack) - n
        print(nthLastIndex)
        if nthLastIndex == 0:
            print("here")
            return head.next
        elif nthLastIndex > 0:
            print("there")
            stack[nthLastIndex - 1].next = stack[nthLastIndex].next
            return head
        else:
            print("everywhere")
            return None




        
        
# @lc code=end

