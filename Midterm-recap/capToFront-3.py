def capToFront(x):
    BB = str(x)
    string = len(BB)
    for i in range(string):
        for j in range(string-1):
            if  BB[j] > BB[j+1]:
                BB = BB[:j] + BB[j+1] + BB[j] + BB[j+2:]

    print("\t\tSorted String : ", BB)
capToFront("hApPy")
capToFront("moveMENT")
capToFront("sh0rtCAKE")                                                                