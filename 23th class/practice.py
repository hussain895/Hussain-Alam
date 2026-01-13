lists = list(map(int,input("Enter Marks Separated By Space : ").split()))
print(lists)
if len(lists) == 0:
    print("Error!,Plese Enter The Number")
else:
    add = sum(lists)
    print("Sum Of The List Is : " , add)
    avg = sum(lists) / len(lists)
    print("Average Of The List : " , avg)
    lists.sort()
    print("Sorted Of The List : ", lists)
    print("Highest Marks : " , max(lists))
    print("Lowest Marks : " , min(lists))