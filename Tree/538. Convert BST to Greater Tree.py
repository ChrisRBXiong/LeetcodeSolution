'''
Recursive
'''
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.greater_sum = 0
        return self.core(root)
   
    def core(self,root):
        if root is None:
            return None
        else:
            self.core(root.right)
            root.val += self.greater_sum
            self.greater_sum = root.val
            self.core(root.left)
            return 

'''
Iterative
'''
class Solution2(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes_s = []
        greater_sum = 0
        curr = root
        while len(nodes_s) or curr:
            if curr:
                nodes_s.append(curr)
                curr = curr.right
            else:
                curr = nodes_s.pop()
                curr.val += greater_sum
                greater_sum = curr.val
                curr = curr.left
        return root
                
            

        