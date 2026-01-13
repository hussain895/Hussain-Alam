arr = [72, 45, 60, 30, 18, 55, 27]

print("Original Array = ", arr)
print()

n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

print("Final Array = ", arr)
