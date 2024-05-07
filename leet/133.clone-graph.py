#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque([node])
        seen = dict()
        while q:
            next = q.popleft()
            if next.val in seen:
                continue
            seen[next.val] = Node(next.val)
            for n in next.neighbors:
                seen[next.val].neighbors.append(Node(n.val))
                q.append(n)
        return seen[node.val]

        
# @lc code=end

