def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
if __name__ == "__main__":
    arr = [12, 4, 56, 1, 78, 33]
    sorted_arr = insertion_sort_descending(arr)
    print("Sorted list (descending):", sorted_arr)
