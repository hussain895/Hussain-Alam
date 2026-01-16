import time
import matplotlib.pyplot as plt

arr = [12, 11, 13, 5, 6]
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
plt.figure(figsize=(10,6))
plt.ion()

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        visualize(arr, j, i)
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print() 
visualize(arr)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:")
    print_array(arr)
    insertionsort(arr)
    print("Sorted array:")
    print_array(arr)
    visualize(arr)
plt.ioff()
plt.show()