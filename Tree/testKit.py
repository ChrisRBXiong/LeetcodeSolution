# Definition for a binary tree node.
from collections import deque
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def draw(self):
        drawtree(self)



            


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
            if left_value is not None:
                left = TreeNode(left_value)
                node.left = left
                nodes_q.append(left)
        if len(values_q):
            right_value = values_q.popleft()
            if right_value is not None:
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


'''Display Tree Part'''
class AsciiNode(object):
    left = None
    right = None

    # length of the edge from this node to its children
    edge_length = 0
    height = 0
    lablen = 0

    # -1 = left, 0 = root, 1 = right
    parent_dir = 0

    # max supported unit32 in dec, 10 digits max
    label = ''

MAX_HEIGHT = 1000
lprofile = [0] * MAX_HEIGHT
rprofile = [0] * MAX_HEIGHT
INFINITY = (1 << 20)

# adjust gap between left and right nodes
gap = 3


def build_ascii_tree_recursive(t):
    """
    :type t: TreeNode
    """
    if t is None:
        return None

    node = AsciiNode()
    node.left = build_ascii_tree_recursive(t.left)
    node.right = build_ascii_tree_recursive(t.right)

    if node.left:
        node.left.parent_dir = -1

    if node.right:
        node.right.parent_dir = 1

    node.label = '{}'.format(t.val)
    node.lablen = len(node.label)
    return node


# Copy the tree into the ascii node structure
def build_ascii_tree(t):
    if t is None:
        return None
    node = build_ascii_tree_recursive(t)
    node.parent_dir = 0
    return node

# The following function fills in the lprofile array for the given tree.
# It assumes that the center of the label of the root of this tree
# is located at a position (x,y).  It assumes that the edge_length
# fields have been computed for this tree.
def compute_lprofile(node, x, y):
    if node is None:
        return

    isleft = (node.parent_dir == -1)
    lprofile[y] = min(lprofile[y], x - ((node.lablen - isleft) // 2))
    if node.left:
        i = 1
        while (i <= node.edge_length and y + i < MAX_HEIGHT):
            lprofile[y + i] = min(lprofile[y + i], x - i)
            i += 1

    compute_lprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_lprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


def compute_rprofile(node, x, y):
    if node is None:
        return

    notleft = (node.parent_dir != -1)
    rprofile[y] = max(rprofile[y], x + ((node.lablen - notleft) // 2))
    if node.right is not None:
        i = 1
        while i <= node.edge_length and y + i < MAX_HEIGHT:
            rprofile[y + i] = max(rprofile[y + i], x + i)
            i += 1

    compute_rprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_rprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


def compute_edge_lengths(node):
    if node is None:
        return
    compute_edge_lengths(node.left)
    compute_edge_lengths(node.right)

    # first fill in the edge_length of node
    if (node.right is None and node.left is None):
        node.edge_length = 0
    else:
        if node.left:
            i = 0
            while (i < node.left.height and i < MAX_HEIGHT):
                rprofile[i] = -INFINITY
                i += 1
            compute_rprofile(node.left, 0, 0)
            hmin = node.left.height
        else:
            hmin = 0

        if node.right is not None:
            i = 0
            while (i < node.right.height and i < MAX_HEIGHT):
                lprofile[i] = INFINITY
                i += 1
            compute_lprofile(node.right, 0, 0)
            hmin = min(node.right.height, hmin)
        else:
            hmin = 0

        delta = 4
        i = 0
        while (i < hmin):
            delta = max(delta, gap + 1 + rprofile[i] - lprofile[i])
            i += 1

        # If the node has two children of height 1, then we allow the
        # two leaves to be within 1, instead of 2
        if (((node.left is not None and node.left.height == 1) or (
                        node.right is not None and node.right.height == 1)) and delta > 4):
            delta -= 1
        node.edge_length = ((delta + 1) // 2) - 1


    # now fill in the height of node
    h = 1
    if node.left:
        h = max(node.left.height + node.edge_length + 1, h)
    if node.right:
        h = max(node.right.height + node.edge_length + 1, h)
    node.height = h


# used for printing next node in the same level,
# this is the x coordinate of the next char printed
print_next = 0

def print_level(node, x, level):
    global print_next
    if node is None:
        return
    isleft = (node.parent_dir == -1)
    if level == 0:
        spaces = (x - print_next - ((node.lablen - isleft) // 2))
        sys.stdout.write(' ' * spaces)

        print_next += spaces
        sys.stdout.write(node.label)
        print_next += node.lablen
    elif node.edge_length >= level:
        if node.left:
            spaces = (x - print_next - level)
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('/')
            print_next += 1

        if node.right:
            spaces = (x - print_next + level)
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('\\')
            print_next += 1
    else:

        print_level(node.left,
                    x - node.edge_length - 1,
                    level - node.edge_length - 1)
        print_level(node.right,
                    x + node.edge_length + 1,
                    level - node.edge_length - 1)


# prints ascii tree for given Tree structure
def drawtree(t):
    if t is None:
        return
    proot = build_ascii_tree(t)
    compute_edge_lengths(proot)
    i = 0
    while (i < proot.height and i < MAX_HEIGHT):
        lprofile[i] = INFINITY
        i += 1

    compute_lprofile(proot, 0, 0)
    xmin = 0
    i = 0
    while (i < proot.height and i < MAX_HEIGHT):
        xmin = min(xmin, lprofile[i])
        i += 1

    i = 0
    global print_next
    while (i < proot.height):
        print_next = 0
        print_level(proot, -xmin, i)
        print()
        i += 1

    if proot.height >= MAX_HEIGHT:
        print("This tree is taller than %d, and may be drawn incorrectly.".format(MAX_HEIGHT))

