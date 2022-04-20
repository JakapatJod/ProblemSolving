def isValidIP(x):
    
    b = str(x)

    Test = False

    if "." in b:
        elements_array = b.strip().split(".")

    if len(elements_array) == 4:
        for i in elements_array:
            
            if i[0] == '0':
                Test = False
                break
            elif i.isnumeric() and int(i)>=0 and int(i)<=255:
                Test = True
            else:
                Test = False
                break
            
    if Test:
        print("True")
    else:
        print("False")


isValidIP("1.2.3.4")
isValidIP("1.2.3") 
isValidIP("1.2.3.4.5")
isValidIP("123.45.67.89") 
isValidIP("123.456.78.90") 
isValidIP("123.045.067.089")     