arr = [12 , 24 , 56, 23]
print("Original Array = " , arr)
n = len(arr)

for step in range(n-1):
    min_index = step
    for i in range(step+1 , n):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[step] , arr[min_index] = arr[min_index] , arr[step]

print("Sorted Array  = ", arr)

