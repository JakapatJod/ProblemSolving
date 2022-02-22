import timeit

MIN_MERGE = 32
 
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
def merge(arr, l, m, r):
     
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
     
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
     
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):
 
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size
 
if __name__ == "__main__":
 
    arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12]
 
    timSort(arr)


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]

def tim_time():
    SETUP_CODE = """from __main__ import timSort"""

    TEST_CODE ="""
nums = [14,45,43,27,57,41,45,21,70]
timSort(nums)
"""
    
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100000)
    print('timSort using time: {}'.format(min(times)))

def bubbleSort_time():
    SETUP_CODE = """from __main__ import bubbleSort"""

    TEST_CODE ="""
nums = [14,45,43,27,57,41,45,21,70]
bubbleSort(nums)
"""
    
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=100000)
    print('BubbleSort using time: {}'.format(min(times)))

if __name__ == "__main__":
    bubbleSort_time()
    tim_time()