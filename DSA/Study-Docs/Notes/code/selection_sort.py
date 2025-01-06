arr = [89, 3, 0, 456, 24, 90]

def find_smallest(in_arr):
    smallest = in_arr[0]
    smallest_idx = 0
    n = len(in_arr)
    for i in range(n):
        if in_arr[i] < smallest:
            smallest = in_arr[i]
            smallest_idx = i
    return smallest, smallest_idx

def selection_sort(in_list):
    n = len(in_list)
    sorted_list = []
    sublist = in_list
    for i in range(n):
        sublist_smallest, sublist_smallest_idx = find_smallest(sublist)
        sublist.pop(sublist_smallest_idx)
        sorted_list.append(sublist_smallest)
    return sorted_list

print(selection_sort(arr))