def reverse_while_loop(s):
    s1 = ''
    lenght = len(s) - 1
    while lenght >= 0:
        s1 = s1 + s[lenght]
        lenght = lenght - 1
    return s1

input_str = 'INE-KMUTNB'
if __name__== "__main__":
    print('Reverse String using while loop = ',reverse_while_loop(input_str))