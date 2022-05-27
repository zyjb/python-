l = [9999, 14, 1, 46, 12, 534, 146, 520, 13, 14, 1314, 4576, 1345, 0.1]


def buble(l: list) -> list:
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


    return l


print(buble(l))
