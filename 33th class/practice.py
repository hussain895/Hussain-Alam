import numpy as np

marks = np.array([
    [78,85,90],
    [20,45,69],
    [30,50,98],
    [40,45,78]
])

print("First Student Marks : " ,marks[0])
print("Second Student Marks : " ,marks[1])
print("Third Student Marks : " ,marks[2])
print("Fourth Student Marks : " ,marks[3])
print()
Total_Marks = marks.sum(axis=1)
print("Total Marks : " , Total_Marks)
print()

lenght = len(marks[0])


avg = Total_Marks/lenght

print("Average Marks : " , avg)
print()

