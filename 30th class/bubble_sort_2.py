arr = [6 , 8 , 5 , 4]
print("Original Array : " , arr)

n = len(arr)

for step in range(n-1):
    for i in range(n-1 - step):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp

print("Sorted Array : " , arr)
