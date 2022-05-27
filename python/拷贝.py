import copy

a = [1,2,3]
# b = copy.deepcopy(a)
b = a
print(id(a),id(b))

x,y,z = 1,1,2
print(id(x),id(y),id(z))
# a.append(4)
# a.append(5)
# print(a,b)