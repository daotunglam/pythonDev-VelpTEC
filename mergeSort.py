def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Teile die Liste in zwei Hälften
    mid = len(arr) // 2
    print('mid',mid, )
    left_half = arr[:mid]
    right_half = arr[mid:]
    print('left',left_half, 'right', right_half)

    # Sortiere die beiden Hälften rekursiv
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Führe die beiden sortierten Hälften zusammen
    merged = merge(left_half, right_half)
    print('merged ', merged)
    return merged

def merge(left, right):
    print(left,right)
    merged = []
    i = j = 0

    # Füge die Elemente aus den beiden Hälften in aufsteigender Reihenfolge zusammen
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Füge die verbleibenden Elemente hinzu
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


print(merge_sort([90, 2, 94, 888, 55, 213, 66]))