# 有一群猴子，去偷了一堆桃子,
# 商量之后决定每天吃剩余桃子的一半,
# 当每天大家吃完桃子之后，有个贪心的小猴都会偷偷再吃一个桃子,
# 按照这样的方式猴子们每天都快乐的吃着桃子
# 直到第十天，当大家再想吃桃子时，发现只剩下一个桃子了
# 问： 最开始有多少个桃子？
# day1 / 2 -1 = day2   [day1=(day2+1)*2]
# day2 / 2 -1 = day3
# .....
# day9 / 2 -1 = day10 = 1   [day9=(day10+1)*2)]

# yesterday = 1
# for i in range(9):
#     today = (yesterday+1)*2
#     yesterday = today
# print(today)

name = 2
print('zhao') if name == 1 else print('li')

# lambda #匿名函数
l = lambda a, b: a * b
print(l(2, 3))
