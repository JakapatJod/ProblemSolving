odd = []
even = []
def bubbleSort(nlist):
    global even,odd        
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

    for n in range(len(nlist)):
        current = nlist[n]
        if current %2 ==0 :
            even.append(current)
        else:
            odd.append(current)

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
nlist = odd + even
print(nlist)