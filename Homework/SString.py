print('')
str = input('\t\tEnter the String : ')

string = len(str)
for i in range(string):
    for j in range(string-1):
        if str[j] > str[j+1]:
            str = str[:j] + str[j+1] + str[j] + str[j+2:]

print("\t\tSorted String : ", str.upper())
print('')