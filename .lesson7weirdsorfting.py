def merge(arr, low, mid, high):
    c = []
    start1 = low
    start2 = mid + 1

    while start1 <= mid and start2 <= high:
        if arr[start1] < arr[start2]:
            c.append(arr[start1])
            start1 += 1
        else:
            c.append(arr[start2])
            start2 += 1

    while start1 <= mid:
        c.append(arr[start1])
        start1 += 1

    while start2 <= high:
        c.append(arr[start2])
        start2 += 1
    k = 0
    for i in range(low, high + 1):
        arr[i] = c[k]
        k += 1

def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


arr = [12,11,13,12,12,3,4,4,5,5,6,7,4,3,231234232,424231,423,4123,,21,4,21,32,1,232,312,54235643567,4,34,,3,43,214,4353,42,32,,34,33,42,4,6,44,3,55,2,66,77]
n = len(arr)
mergesort(arr, 0, n - 1)
print(arr)