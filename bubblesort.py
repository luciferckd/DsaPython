def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n- i - 1):
            if arr[i] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True

        if not swapped:
            break

arr = [64, 34, 54, 64, 22, 65, 86, 42]
bubble_sort(arr)
print("sorted array is: ", arr)

