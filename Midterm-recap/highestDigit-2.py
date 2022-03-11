arr = []
def highestDigit(x):
    global arr
    BB = str(x)
    for K in BB:
        arr.append(K)
    z = max(arr)
    print('highest Digit : ',z)

highestDigit(379)
highestDigit(2)
highestDigit(377401)