'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''
from testKit import *

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.is_valid = True
        self.valid(root)
        return self.is_valid

    def valid(self,root):
        if not root:
            return None, None
        left_min, left_max = self.valid(root.left)
        right_min, right_max = self.valid(root.right)
        legal_min, legal_max = root.val, root.val

        if root.left:
            if left_max >= root.val:
                self.is_valid = False
            legal_min = left_min

        if root.right:
            if right_min <= root.val:
                self.is_valid = False
            legal_max = right_max
        
        return legal_min, legal_max



class Solution2(object):
    '''
    recursive
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = None
        return self.valid(root)
    
    def valid(self,root):
        if root:
            if not self.valid(root.left):
                return False

            if self.pre is not None and self.pre >= root.val:
                return False
            self.pre = root.val
            
            if not self.valid(root.right):
                return False

        return True
            
                
class Solution3(object):
    '''iterative'''

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes_q = []
        curr, pre = root, None
        while len(nodes_q) or curr:
            if curr:
                nodes_q.append(curr)
                curr = curr.left
            else:
                curr = nodes_q.pop()
                if pre and pre.val >= curr.val:
                    return False
                pre = curr
                curr = curr.right
        return True
                
    

        
        


            
