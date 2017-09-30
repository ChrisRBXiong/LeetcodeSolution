"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

class UFS:
    '''
    Path compress and connect by rank
    '''
    def __init__(self, size):
        self.ufs = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
    
    def find(self, x):
        # find ancestor and do path compressing
        px = self.ufs[x]
        while px != self.ufs[px]:
            px = self.ufs[px]
        tx = x
        while tx != px:
            tx, self.ufs[tx] = self.ufs[tx], px
        return px
    
    def connect(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.ufs[py] = px
            else:
                self.ufs[px] = py
                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        xmax, ymax = len(board[0]), len(board)
        ufs = UFS(ymax * xmax + 1)
        dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
        for y in range(ymax):
            for x in range(xmax):
                if board[y][x] == 'O':
                    for d in range(4):
                        ty, tx = y + dy[d], x + dx[d]
                        if ty < 0 or ty >= ymax or tx < 0 or tx >= xmax:
                            try:
                                ufs.connect(y * xmax + x, ymax * xmax)
                            except:
                                return
                            break
                        elif board[ty][tx] == 'O':
                            ufs.connect(y * xmax + x, ty * ymax + tx)
        # do Draw
        for y in range(ymax):
            new_string = []
            for x in range(xmax):
                if board[y][x] == 'O' and not ufs.isConnected(y * xmax + x, ymax * xmax):
                    new_string.append('X')
                else:
                    new_string.append(board[y][x])
            board[y] = "".join(new_string)