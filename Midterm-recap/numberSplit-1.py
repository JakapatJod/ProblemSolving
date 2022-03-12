def numberSplit(x) :

    if x > 0 :

        for i in range(x) :

            if i + i == x : 
                return print([i , i])
            if i + (i + 1) == x : 
                return print([i , i+1])

    else : 

        index = 0

        while True :

            if index + index == x : 
                return print([index , index])
            if index + (index - 1) == x : 
                return print ([index-1 , index])

            index -= 1

numberSplit(4)
numberSplit(10)
numberSplit(-9)

