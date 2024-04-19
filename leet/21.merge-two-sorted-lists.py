#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head = cur

        while list1 or list2:
            if not list2:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            elif not list1:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            elif list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        
        return head.next


        
# @lc code=end

