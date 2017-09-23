class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.curr = root
        right = root.right
        if root.left:
            self.curr.right = root.left
            self.flatten(root.left)
            root.left = None
        if right:
            self.curr.right = right
            self.flatten(right)
