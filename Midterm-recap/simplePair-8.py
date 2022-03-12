def simplePair(datas , number) :

    for i in range(len(datas) - 1) :

        if datas[i] * datas[1] == number : 
            return print([datas[i] , datas[1]])
        if datas[i] * datas[-1] == number : 
            return print([datas[i] , datas[-1]])

    return print('null')


simplePair([1 , 2 , 3] , 3)
simplePair([1 , 2 , 3] , 6)
simplePair([1 , 2 , 3] , 9)