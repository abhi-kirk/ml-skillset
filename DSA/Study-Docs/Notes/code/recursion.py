arr = [1, 2, 3, 4]

def rec_sum(a):
    if a == []:
        return 0
    return a[0] + rec_sum(a[1:])

def count_items(a):
    if a == []:
        return 0
    return 1 + count_items(a[1:])

def max_number(a):
    if len(a) == 2:
        return a[0] if a[0] > a[1] else a[1]
    sub_max = max_number(a[1:])
    return a[0] if a[0] > sub_max else sub_max

print(count_items(arr))