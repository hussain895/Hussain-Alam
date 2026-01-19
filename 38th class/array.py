numbers = [5 , 2 , 9 , 1 , 6]
print("Array Elements:")

for i in range(len(numbers)):
    print(f"Element at index {i}: {numbers[i]}")

numbers[2]  = 7
print("Updated Array" , numbers)

def search_element(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

idx = search_element(numbers, 7)
print("Index of 7 is:" , idx)

def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def find_min(arr):
    min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

max_value = find_max(numbers)
min_value = find_min(numbers)
print(f"Maximum Value: {max_value} And The Index of Maximum Value is: {numbers.index(max_value)}")
print(f"Minimum Value: {min_value} And The  Index of Minimum Value is: {numbers.index(min_value)}")