def binary_search(arr, target, low, high):
    if low > high:
        return 0
     
    mid = (high+low)//2 
    if arr[mid] == target:
     return mid
    elif arr[mid] > target:
       return binary_search(arr, target, low, mid-1)
    else:
       return binary_search(arr, target, mid+1, high)

arr = [1,2,4,6,7,8,9]
target_index =binary_search(arr, 9, 0, len(arr)-1)
print(target_index)


    
