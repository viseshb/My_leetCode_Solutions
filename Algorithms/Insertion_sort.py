def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i-1] > arr[i] and i>0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i-=1

arr = [1,7,3,8,2,5]
insertion_sort(arr)
print(arr)            


