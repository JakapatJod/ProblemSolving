hr = 0
pay = 0
gross = 0
def read():
    global hr , pay
    hr = int(input('\tEnter hours of work : '))
    pay = int(input('\tEnter payout rate : '))
    return hr , pay
def Cal():
    global hr , pay , gross
    gross = hr * pay
    return gross
def Print():
    global gross
    print("\tํYour income : ",gross)
def control():
   again = 'y'
   while again == 'y' :
        read()
        Cal()
        Print()
        again = input('\tEnter y : ')
control()