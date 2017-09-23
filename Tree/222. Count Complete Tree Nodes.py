'''
Given a complete binary tree, count the number of nodes.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

from testKit import *


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.leaf_count = 0
        self.count(root,0)

        return 2 ** self.max_depth + self.leaf_count - 1
    
    def count(self,root,depth):
        if root:
            if self.count(root.left,depth+1):
                return True
            if self.count(root.right,depth+1):
                return True
            if not root.left and not root.right:    #leaf
                if depth < self.max_depth:
                    return True
                self.leaf_count += 1
                self.max_depth = depth

class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l, r = root, root
        lh, rh = 0, 0
        while l is not None:
            lh += 1
            l = l.left
        while r is not None:
            rh += 1
            r = r.right
        if lh == rh:
            return 2 ** lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        


tree = createTree([1,2,3,4,5,6,7,8,9,10,11])
print(Solution2().countNodes(tree))

        