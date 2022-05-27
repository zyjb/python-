#
import random


def random_n():
    return random.randrange(100,1000)
def random_l():
    length = random.randrange(20, 40)
    return random.randrange(10,length)

nums = []
for i in range(random_l()):
    nums.append(random_n())
print(nums)
# print(len(nums))
# print(range(len(nums)))
# 冒泡排序

for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j]>=nums[j+1]:
            a = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = a
# print(nums)

# 归并排序

# 快速排序
# def _sum(a:list,b:int): #整数加减
#     return a+b
#
# print(_sum(1.1,2.2))
def sum(a:list[int],b:list[int])->list[int]:
    pass