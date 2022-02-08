import timeit
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]
    
def reverse_string_join(s):
    s1 = ''.join(reversed(s))
    return s1

def reverse_slicing(s):
    return s[::-1]

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def reverse_while_loop(s):
    s1 = ''
    lenght = len(s) - 1

    while lenght >= 0:
        s1 =s1 +s[lenght]
        lenght = lenght -1
    return s1

def reverse_for_loop(s):
    s1 = ''
    
    for c in s:
        s1 = c + s1 
    return s1



def slicing_time():
    SETUP_CODE_FOR = """from __main__ import reverse_for_loop"""
    SETUP_CODE_WHILE = """from __main__ import reverse_while_loop"""
    SETUP_CODE_JOIN = """from __main__ import reverse_string_join"""
    SETUP_CODE_RECURSION = """from __main__ import reverse_recursion"""
    SETUP_CODE_REVERSE = """from __main__ import reverse_slicing"""
    SETUP_CODE_LIST = """from __main__ import reverse_slicing"""
    

    TEST_CODE_FOR ="""
input_str = 'INE-KMUTNB'
reverse_for_loop(input_str)
"""
    TEST_CODE_WHILE ="""
input_str = 'INE-KMUTNB'
reverse_while_loop(input_str)
"""
    TEST_CODE_JOIN ="""
input_str = 'INE-KMUTNB'
reverse_string_join(input_str)
"""
    TEST_CODE_RECURSION ="""
input_str = 'INE-KMUTNB'
reverse_recursion(input_str)
"""
    TEST_CODE_REVERSE ="""
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
"""
    TEST_CODE_LIST ="""
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
"""
    list_time = ()
    
    times_for = timeit.repeat(setup=SETUP_CODE_FOR, stmt=TEST_CODE_FOR, repeat=3, number=10000)
    print('Reverse String using for loop: {}'.format(min(times_for)))

    times_while = timeit.repeat(setup=SETUP_CODE_WHILE, stmt=TEST_CODE_WHILE, repeat=3, number=10000)
    print('Reverse String using while loop: {}'.format(min(times_while)))

    
    times_join = timeit.repeat(setup=SETUP_CODE_JOIN, stmt=TEST_CODE_JOIN, repeat=3, number=10000)
    print('Reverse String using join: {}'.format(min(times_join)))
    
    times_recursion = timeit.repeat(setup=SETUP_CODE_RECURSION, stmt=TEST_CODE_RECURSION, repeat=3, number=10000)
    print('Reverse String using recursion: {}'.format(min(times_recursion)))

    times_reverse = timeit.repeat(setup=SETUP_CODE_REVERSE, stmt=TEST_CODE_REVERSE, repeat=3, number=10000)
    print('Reverse String using reverse: {}'.format(min(times_reverse)))

    times_list = timeit.repeat(setup=SETUP_CODE_LIST, stmt=TEST_CODE_LIST, repeat=3, number=10000)
    print('Reverse String using list: {}'.format(min(times_list)))


if __name__ == "__main__":
    slicing_time()
    
    