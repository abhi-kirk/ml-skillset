arr = [5, 89, 450, 908, 1024]

def binary_search(in_list, x):
    low, high = 0, len(in_list)-1
    while low <= high:
        mid = (low+high)//2
        guess = in_list[mid]
        if guess < x:
            low = mid+1
        elif guess > x:
            high = mid-1
        else:
            return mid
    return None

num_to_search = int(input("Enter number to search: "))
print(binary_search(arr, num_to_search))
