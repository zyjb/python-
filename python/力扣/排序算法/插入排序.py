l = [9999, 14, 1, 46, 12, 534, 146, 520, 13, 14, 1314, 4576, 1345]
import random as rd
import copy

l1 = [rd.randint(0, 10000000) for i in range(100000)]
l2 = copy.copy(l1)
# print(len(l1))


def insertion_sort(l):
    cur = 0
    for i in range(1, len(l)):
        idx = i
        while l[idx] < l[idx - 1] and idx > 0:
            l[idx], l[idx - 1] = l[idx - 1], l[idx]
            idx -= 1
            cur += 1
    print(cur)


# 247592
# insertion_sort(l2)


# def insert_sort(l):
#     cur = 0
#     for i in range(1, len(l)):
#         temp = l[i]
#         idx = i-1
#         while idx >= 0 and temp < l[idx]:
#             l[idx + 1] = l[idx]
#             idx -= 1
#             cur += 1
#         l[idx+1] = temp
#     print(cur)
# insert_sort(l2)



