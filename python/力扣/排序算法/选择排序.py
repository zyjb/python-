l = [9999, 14, 1, 46, 12, 534, 146, 520, 13, 14, 1314, 4576, 1345, 0.1]


def select_sort(l):

    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

    print(l)

select_sort(l)
