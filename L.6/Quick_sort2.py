from numpy import array


def partition(array,begin,end):
    pivot = begin
    for i in range(begin+1,end+1):
        if array[i] <= array[begin]:
            pivot += 1 
            array[i],array[pivot] = array[pivot],array[i]
    array[pivot],array[begin] = array[begin],array[pivot]
    return pivot

def quicksort(array,begin=0,end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array,begin,end):
        if begin >= end:
            return
        pivot = partition(array,begin,end)
        _quicksort(array,begin,pivot-1)
        _quicksort(array,pivot+1,end)
    return _quicksort(array,begin,end)

array = [14,46,43,27,57,41,45,21,70]
quicksort(array)
print(array)