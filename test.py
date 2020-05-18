# # class Solution:
# #     def solve(self , n , m , a ):
# #         l, r = 1, min(a)
# #         while l < r:
# #             mid = l + (r-l) // 2
# #             cnt = self.helper(a, mid)
# #             if cnt >= m:
# #                 l = mid + 1
# #             else:
# #                 r = mid 
# #         # return res
# #         cnt = self.helper(a, l)
# #         if cnt < m:
# #            return l - 1
# #         else:
# #            return l

# #     def helper(self, a, min_count):
# #         array = a 
# #         cnt = 0
# #         for a in array:
# #             cnt += a // min_count
# #         return cnt 


# # Solution().solve(3,5,[3,5,6])





# class Solution:
#     def function(self, arrays, n, d):
#         if n == 0:
#             return 0
#         arrays = sorted(arrays)
#         cur = arrays[0]
#         count = 1
#         for n in arrays:
#             if n - cur >= d:
#                 cur = n 
#                 count += 1
#         return count 


# print(Solution().function([1,4,2,8,5,7],6,2))

        
import numpy as np
a = np.array([83,94,77,79,80,90,90,96,95,87,92,96,83,85])
b = np.array([1,1,3,2,2,1,1,1,3,3,2,2,3,2])
assert len(a) == len(b)
c = np.sum(a * b)
print(c/sum(b))



        