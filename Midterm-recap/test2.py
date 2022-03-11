SS = []
def numberSplit(x):
    global SS
    p = x//2
    z = x%2

    if z == 0:
        SS = [p,z]
    print(SS)
numberSplit(12)