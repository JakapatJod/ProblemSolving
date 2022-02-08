import array

a = array.array('i',[1,2,3])
b = array.array('i',[4,5,6])
a.extend(b)
print(a)
print(a[3])