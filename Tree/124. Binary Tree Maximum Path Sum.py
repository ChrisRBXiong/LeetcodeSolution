"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
from testKit import *

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = None
        self.maxPathSumRecursive(root)
        return self.max_sum

    def maxPathSumRecursive(self,root):
        if not root: return 0
        left = self.maxPathSumRecursive(root.left)
        right = self.maxPaumRecursive(root.right)

        if self.max_sum is None:
            self.max_sum = left + right + root.val
        self.max_sum = max(self.max_sum, left + right + root.val)

        return max(0, root.val + max(left,right))
        
