import time
import matplotlib.pyplot as plt

arr = [38 , 27 , 43, 10 , 12 , 17]
def visualize(arr , idx1 = None , idx2 = None):
    plt.clf()
    colors = ['blue'] * len(arr)
    if idx1 is not None:
        colors[idx1] = 'red'
    if idx2 is not None:
        colors[idx2] = 'green'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.xticks(range(len(arr)), arr)
    plt.title("Array Visualization")
    plt.pause(0.5)

def merge(arr , left , mid , right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * (n1)
    R = [0] * (n2)
    visualize(arr, left, right)
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    visualize(arr, left, right)
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    visualize(arr, left, right)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
plt.figure(figsize=(10,6))
plt.ion()

def mergeSort(arr , left , right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        visualize(arr, left, right)

if __name__ == "__main__":
    arr = [38 , 27 , 43, 10 , 12 , 17]
    print("Given array is:", arr)
    mergeSort(arr, 0, len(arr) - 1)
    if arr == sorted(arr):
        print("Sorted array is:", arr)
visualize(arr)
plt.ioff()
plt.show()

