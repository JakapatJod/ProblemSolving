def getBudgets(datas) : 

    return print(datas[0]['badget'] + datas[1]['badget'] + datas[2]['badget'])

name = 'name'
age = 'age'
budget = 'badget'

getBudgets([

    {name : "John" , age : 21 , budget : 23000} ,
    {name : "Steve" , age : 32 , budget : 40000} ,
    {name : "Martin" , age : 16 , budget : 2700}])

getBudgets([

    {name : "John" , age : 21 , budget : 29000} ,
    {name : "Steve" , age : 32 , budget : 32000} ,
    {name : "Martin" , age : 16 , budget : 1600}])