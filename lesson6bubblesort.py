def bubble_sort(arr):
    n = len(arr)
 # traver through all elemetns in the array
    
    for i in range(n):
        swapped = False

        ### last i elemet are already in place no need to check them
        for j in range(0, n - i - 1):
            #if the current elemet is greatwe swap them
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True
        if not swapped:
            break





#example list of numbers
number = [12,45,34,5,6,5,3,2,5,4,5,6,99]
#prony thiss original list
print("origanal list ",number)


bubble_sort(number)
print("sorted list ",number)


