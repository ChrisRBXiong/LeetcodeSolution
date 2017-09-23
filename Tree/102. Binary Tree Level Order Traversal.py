"""
Given a binary tree, return the level order traversal of its nodes' values
"""
from collections import deque
from testKit import *

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes_q, traversal = deque(), []
        if root: nodes_q.append((root,0))
        max_depth = -1
        while nodes_q:
            curr, depth = nodes_q.popleft()
            if depth > max_depth: 
                max_depth = depth
                traversal.append([])
            traversal[depth].append(curr.val)
            if curr.left: nodes_q.append((curr.left,depth+1))
            if curr.right: nodes_q.append((curr.right,depth+1))
        return traversal
            