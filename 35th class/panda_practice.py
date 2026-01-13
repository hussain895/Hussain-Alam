import pandas as pd

marks = pd.Series({"Math" : 80 , "Science" : 85 , "English" : 78})
marks = marks + 5
print(marks)
print()

print("-----------------------------------------------------Access Only One Subject's Marks---------------------------------------------------------------")
print()
print(f"Science : " ,marks[1])
print()

print("--------------------------------------------------Find Sum And Average Of All Subject's Marks----------------------------------------------------")
print()
Sum = sum(marks)
print(f"Sum Of All Subject's Marks : " , Sum)
Len = len(marks)
print(f"Average Of All Subject's Marks : " , Sum/Len )
print()
print("-----------------------------------------------------Find Highest And Lowest Marks------------------------------------------------------------------")
print()
print(f"Highest Marks : " , marks.max())
print(f"Lowest Marks : " , marks.min())