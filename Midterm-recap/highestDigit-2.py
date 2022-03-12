def highestDigit(x):

    BB = str(x)
    arr = []
    for K in BB:
        arr.append(K)
    z = max(arr)
    print('highest Digit : ',z)

highestDigit(379)
highestDigit(2)
highestDigit(377401)