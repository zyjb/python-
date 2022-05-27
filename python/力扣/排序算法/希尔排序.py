import random as rd
l1 = [rd.randint(0, 100) for i in range(10)]
print(l1)
def shellSort(l1):
    n = len(l1)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = l1[i]
            j = i
            while j >= gap and l1[j - gap] > temp:
               l1[j] = l1[j - gap]
               j -= gap
            l1[j] = temp
        gap = gap // 2
    print(l1)

shellSort(l1)