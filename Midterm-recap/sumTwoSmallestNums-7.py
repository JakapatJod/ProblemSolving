def sumTwoSmallestNums(x):
    low1 = x[0] 
    low2 = None
    for i in x[1:]:     
        
        if i < low1: 
            low2 = low1
            low1 = i
        elif low2 == None or low2 > i: 
            low2 = i 
              
    Ans = low1+low2
    print('Answer : ',Ans)
    
sumTwoSmallestNums([19,5,42,2,77])
sumTwoSmallestNums([10,343445353,3453445,345354353453])
sumTwoSmallestNums([2,9,6,-1])
sumTwoSmallestNums([879,953,694,-847,342,221,-91,-723,791,-587])
sumTwoSmallestNums([3689,2902,3951,-475,1617,-2385])