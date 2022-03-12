def sumTwoSmallestNums(x) :

    x.sort()

    if x[0] > 0 : 
        return print('result : ',x[0] + x[1])
    else : 

        for i in range(len(x)) :

            if x[0] < 0 : x.pop(0)
        
        return print('result : ',x[0] + x[1])
    
sumTwoSmallestNums([19,5,42,2,77])
sumTwoSmallestNums([10,343445353,3453445,345354353453])
sumTwoSmallestNums([2,9,6,-1])
sumTwoSmallestNums([879,953,694,-847,342,221,-91,-723,791,-587])
sumTwoSmallestNums([3689,2902,3951,-475,1617,-2385])