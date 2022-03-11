def removeDups(x):
    POP = []
    for i in x:
        if i not in POP:
            POP.append(i)
    print('remove dups : ',str(POP))

removeDups([1,0,1,0])
removeDups(['The','big','cat'])
removeDups(['John','Taylor','John'])

