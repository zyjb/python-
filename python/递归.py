# 1 1 2 3 5 8 ………………
#fn = f(n-1)+f(n-2)  n>2
#fn = 1              n<=2
# 斐波那契数列问题
# def Fb(n):
#     if n<=2:
#         return 1
#     else:
#         return Fb(n-1)+Fb(n-2)
# for i in range(1,5):
#     print(Fb(i),end='   ')

# 汉诺塔问题#
# def h(n,a,b,c):
#     if n==1:
#         print(a+'->'+c)
#         return
#     h(n-1,a,c,b) # A,C,B  # 1  3  2
#     h(1,a,b,c)
#     h(n-1,b,a,c)
# h(2,'1','2','3')

# 阶乘
# def w(n):
#     if n==1:
#         return 1
#     return n*w(n-1)
#
# print(w(5))
# '''
#     1    1   1   1   1
#     2    2   1   3   1
#     1    2   2   2   1
#     1    0   1   2   2
#     1    0   1   3   1
#     1    1   1   1   1
# '''