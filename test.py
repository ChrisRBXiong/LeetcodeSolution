# class Solution:
#     def solve(self , n , m , a ):
#         l, r = 1, min(a)
#         while l < r:
#             mid = l + (r-l) // 2
#             cnt = self.helper(a, mid)
#             if cnt >= m:
#                 l = mid + 1
#             else:
#                 r = mid 
#         # return res
#         cnt = self.helper(a, l)
#         if cnt < m:
#            return l - 1
#         else:
#            return l

#     def helper(self, a, min_count):
#         array = a 
#         cnt = 0
#         for a in array:
#             cnt += a // min_count
#         return cnt 


# Solution().solve(3,5,[3,5,6])



def function(k):
    s, not_s = 1, 0
    for i in range(k):
        prev_s, prev_not_s = s, not_s
        not_s = prev_s + 2*prev_not_s
        s = 3*prev_not_s
        s, not_s = prev_s, prev_not_s
    return s 



        