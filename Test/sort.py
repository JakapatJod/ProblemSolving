list = []
number = int(input("\tPlease Enter the Total Number of Elements : "))
for i in range(number):
    value = input("Please enter the %d Element of List1 : " %i)
    list.append(value)

for i in range(number - 1):
    for a in range(number - i - 1):
        if list[a] > list[a + 1]:
            t = list[a]
            list[a] = list[a + 1]
            list[a + 1] = t
print('\tttt')
print('Sorted List  : ', list)