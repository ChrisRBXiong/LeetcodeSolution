"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        if self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val):
            return True
        return False
    
from testKit import *
tree = createTree([10,5,-3,3,2,None,11,3,-2,None,1])
tree.draw()