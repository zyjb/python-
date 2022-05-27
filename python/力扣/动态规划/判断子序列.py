# # class Solution:
# #     def isSubsequence(self, s: str, t: str) -> bool:
# #         loc = -1
# #         for a in s:
# #             loc = t.find(a, loc + 1)
# #             print(loc)
# #             if loc == -1:
# #                 return False
# #         return True
# #
# # s = Solution()
# # print(s.isSubsequence('abc','cba'))
#
#
# # coding=utf-8
# class BinarySearch(object):
#     def binary_search(self, array, data):
#         """二分查找法递归实现"""
#         if len(array) == 0:
#             return False
#         array.sort()
#         mid_index = len(array) // 2
#         if array[mid_index] == data:
#             return True
#         return self.binary_search(array[mid_index + 1:], data) if data > array[mid_index] else \
#             self.binary_search(array[:mid_index], data)
#
# if __name__ == '__main__':
#     array = [50, 77, 55, 29, 10, 30, 66, 18, 80, 51]
#     search = BinarySearch()
#     print('搜索结果：', search.binary_search(array, 77))
#     print('搜索结果：', search.binary_search(array, 777))
#
#
#
l = [3, 4, 2, 5, 6, 7, 1, 9, 8, 4]
l.sort()
print(l)
