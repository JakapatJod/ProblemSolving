def numberSplit(x):
    D = []
    if x % 2 == 0:
        x = format(x/2,".0f")
        s = x
    elif x %2 != 0:
        #x = int(format(x/2,".0f"))
        x = x/2
        z = int(format(x,".0f"))
        s = x+1
        s = format(s,".0f")
        print(z)
    D.append(z)
    D.append(s)
    print('NumberSplit : ',D)

numberSplit(4)
numberSplit(10)
numberSplit(-9)

