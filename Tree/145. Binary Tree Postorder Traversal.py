from testKit import *
"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""

"""
Iterative Preorder Traversal 
"""
def preorder(tree):
    node_s, traversal = [tree], []
    while len(node_s) > 0:
        n = node_s.pop()
        traversal.append(n.val)
        if n.right: node_s.append(n.right)
        if n.left: node_s.append(n.left)
    return traversal

def inorder(tree):
    node_s, traversal = [], []
    while tree is not None:
        node_s.append(tree)
        tree = tree.left
    while len(node_s) > 0:       #Start travesal
        n = node_s.pop()
        traversal.append(n.val)
        if n.right:
            n = n.right
            while n is not None:
                node_s.append(n)
                n = n.left
    return traversal

def postorder(tree):
    node_s, traversal = [], []
    while tree is not None:
        node_s.append((tree,0))
        tree = tree.left
    while len(node_s) > 0:
        n, tag = node_s.pop()
        if tag == 0:
            node_s.append((n,1))
            if n.right:
                n = n.right
                while n is not None:
                    node_s.append((n,0))
                    n = n.left
        else:
            traversal.append(n.val)
    return traversal


def preorder2(tree):
    node_s, traversal = [], []
    curr = tree
    while len(node_s) > 0 or not curr is None:
        if not curr is None:
            traversal.append(curr.val)
            node_s.append(curr)
            curr = curr.left
        else:
            curr = node_s.pop().right
    return traversal

def inorder2(tree):
    node_s, traversal = [], []
    curr = tree
    while len(node_s) > 0 or not curr is None:
        if not curr is None:
            node_s.append(curr)
            curr = curr.left
        else:
            curr = node_s.pop()
            traversal.append(curr.val)                        
            curr = curr.right
    return traversal

def postorder2(tree):
    node_s, traversal = [], []
    curr = tree
    while len(node_s) > 0 or not curr is None:
        if not curr is None:
            node_s.append(curr)
            curr = curr.left
        else:
            curr = node_s.pop()
            curr = curr.right
    return traversal  
            
        


