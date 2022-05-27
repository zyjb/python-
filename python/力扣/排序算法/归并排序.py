import random as rd

l1 = [rd.randint(0, 100000000) for i in range(1000000)]


cur = 0

def merge_sort(l):
    if len(l) == 1:
        return l
    gap = len(l) // 2
    left = merge_sort(l[:gap])
    right = merge_sort(l[gap:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    global cur
    l = r = 0
    results = []
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            results.append(right[r])
            r += 1
            cur += 1
        else:
            results.append(left[l])
            l += 1
            cur += 1
    results += left[l:]
    results += right[r:]
    return results

print(merge_sort(l1))
print(cur)