def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(left, 'pivot', pivot, right)

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([90, 2, 94, 888, 55, 213, 66]))