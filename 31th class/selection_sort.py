# arr = [72 , 45 , 60 , 30 , 18 , 55 , 27]


# print("Original Array = " , arr)
# print()
# n = len(arr)
# for step in range(n - 1):
#     min_index = step
#     for i in range(step+1 ,n):
#         if arr[i] < arr[min_index]:
#             min_index = i
            
#     arr[step], arr[min_index] = arr[min_index], arr[step]
# print("Final Array = " , arr)


import time
import matplotlib.pyplot as plt

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


arr = [72 , 45 , 60 , 30 , 18 , 55 , 27]


print("Original Array = " , arr)
print()
n = len(arr)
visualize(arr)
for step in range(n - 1):
    min_index = step
    for i in range(step+1 ,n):
        if arr[i] < arr[min_index]:
            min_index = i
            visualize(arr, step, min_index)
    arr[step], arr[min_index] = arr[min_index], arr[step]
print("Final Array = " , arr)
visualize(arr, step, min_index)
plt.ioff()
plt.show()