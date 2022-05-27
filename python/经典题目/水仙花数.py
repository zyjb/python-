'''
三位数  ==百位数三次方+十位数三次方+个位数三次方
'''
# for i in range(100,1000):
#     x=i//100
#     y=i//10%10
#     z=i%10
#     if x**3+y**3+z**3 == i:
#         print(i)


'''
1-100的和
'''
# print(sum(range(1, 101)))
'''
1-100奇数/偶数的和
'''
# print(sum(range(1, 101, 2)))
# print(sum(range(2, 101, 2)))
'''
用while循环输出1，2，3，4，5，6，7，8，9，10
'''
# a = 1
# while a < 11:
#     print(a, end=" ")
#     a += 1
# print()

'''
求1-2+3-4+5-6...+99的和
'''
# a = (sum(range(1, 101, 2)))
# b = (sum(range(2, 100, 2)))
# print(a-b)

'''
打印99乘法表
'''
# a = 1
# b = 0
# while a <= 9:
#     print(a*a, end=" ")
#     a += 1
for i in range(1, 10):
    for j in range(i, i+1):
        print()



