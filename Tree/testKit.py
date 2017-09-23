# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(hr):
    '''
    Input: [1,2,3,None,4]
    Output Tree:
          1
        /   \
        2     3
        \  
        4 
    Input: [1,2,3,None,4,None,None,None,5]
    Output Tree:
        1
      /   \
     2     3
     \
     4
     \
      5 
    ''' 
    if len(hr) == 0 or hr is None:  return None
    nodes_q, values_q = deque(), deque(hr)
    tree = TreeNode(hr[0])
    nodes_q.append(tree)
    values_q.popleft()

    while len(nodes_q) > 0:
        node = nodes_q.popleft()
        if len(values_q):
            left_value = values_q.popleft()
            if left_value:
                left = TreeNode(left_value)
                node.left = left
                nodes_q.append(left)
        if len(values_q):
            right_value = values_q.popleft()
            if right_value:
                right = TreeNode(right_value)
                node.right = right
                nodes_q.append(right)
    return tree

def pre_order(tree):
    if tree:
        print(tree.val)
        pre_order(tree.left)
        pre_order(tree.right)

def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.val)
        in_order(tree.right)

def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.val)


    
    
