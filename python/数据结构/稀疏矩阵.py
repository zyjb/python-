# 压缩文件
l1 = [  [1,2,0,1,0],
        [0,3,0,1,0],
        [1,1,4,0,0],
      ]
#(i,j,k)
l2 = []



for i,v in enumerate(l1):
    for i1,v1 in enumerate(v):
        if v1 != 0:
            l2.append((i,i1,v1))
print(l2)






