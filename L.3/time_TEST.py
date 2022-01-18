import timeit

def reverse_slicing(s):
    return s[::-1]

def slicing_time():
    SETUP_CODE = """ 
from __main__ import reverse_slicing 
"""
    TEST_CODE = """ 
input_str = 'INE-KMUTNB' 
reverse_slicing(input_str) 
"""

    times = timeit.repeat(setup=SETUP_CODE,stmt=TEST_CODE,repeat=3,number=10000)
    print(times)
    print('Slicing time: {}'.format(min(times)))

x = timeit.repeat
if __name__ == "__main__":
    slicing_time()