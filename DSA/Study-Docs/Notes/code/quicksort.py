arr = [7, 3, 90, 1, 0, 4]

def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)

print(qsort(arr))