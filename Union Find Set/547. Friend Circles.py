"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count, ufs, rank = len(M), list(range(len(M))), [0 for i in range(len(M))]
        for i in range(count):
            for j in range(i+1, count):
                if M[i][j]:
                    # do union
                    i_p, j_p = i, j
                    while ufs[i_p] != i_p: i_p = ufs[i_p]
                    while ufs[j_p] != j_p: j_p = ufs[j_p]
                    ufs[i_p] = j_p
                    # do compress(not the standard, directly point to j_p)
                    i_t, j_t = i, j
                    while ufs[i_t] != i_t: i_t, ufs[i_t] = ufs[i_t], j_p
                    while ufs[j_t] != j_t: j_t, ufs[j_t] = ufs[j_t], j_p
        return sum(idx == parent for idx, parent in enumerate(ufs))

print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))







                    
 