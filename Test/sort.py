list = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    list.append(value)

for i in range(number - 1):
    for a in range(number - i - 1):
        if list[a] > list[a + 1]:
            t = list[a]
            list[a] = list[a + 1]
            list[a + 1] = t

print('Sorted List  : ', list)