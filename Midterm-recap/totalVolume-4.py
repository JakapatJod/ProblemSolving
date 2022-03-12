def totalVolume(*datas) : 

    result = 0

    for i in range(len(datas)) :

        result += datas[i][0] * datas[i][1] * datas[i][2]

    return print(result)

totalVolume([4 , 2 , 4] , [3 , 3 , 3] , [1 , 1 , 2] , [2 , 1 , 1])
totalVolume([2 , 2 , 2] , [2 , 1 , 1])
totalVolume([1 , 1 , 1])